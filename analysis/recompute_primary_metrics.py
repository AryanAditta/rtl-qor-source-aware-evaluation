#!/usr/bin/env python3
"""Recompute the manuscript's primary released prediction-level metrics.

This script does not fit a model, regenerate a feature, rerun synthesis/STA or
change any label. It reads only the compact frozen prediction tables released
with this repository.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT / "data" / "fresh_primary_predictions.csv"
EXTERNAL = ROOT / "data" / "external83_primary_predictions.csv"


def basic_metrics(y, pred):
    y = np.asarray(y, dtype=float)
    pred = np.asarray(pred, dtype=float)
    err = pred - y
    mae = np.mean(np.abs(err))
    rmse = np.sqrt(np.mean(err**2))
    sst = np.sum((y - np.mean(y)) ** 2)
    r2 = 1.0 - np.sum(err**2) / sst
    pearson = pearsonr(y, pred).statistic
    spearman = spearmanr(y, pred).statistic
    logerr = np.abs(np.log1p(pred) - np.log1p(y))
    mdape = np.median(np.abs(err) / y) * 100.0
    within10 = int(np.sum(np.abs(err) <= 0.10 * y))
    within20 = int(np.sum(np.abs(err) <= 0.20 * y))
    return {
        "n": len(y),
        "MAE": mae,
        "RMSE": rmse,
        "raw_R2": r2,
        "Pearson_r": pearson,
        "Spearman_rho": spearman,
        "macro_log1p": np.mean(logerr),  # released primary cohorts: one row/component
        "MdAPE_percent": mdape,
        "within_10pct": within10,
        "within_20pct": within20,
    }


def fresh_endpoint(df, cohort, bootstrap_seed):
    x = df.loc[df["cohort"].eq(cohort)].copy()
    if len(x) != 39 or x["source_component"].nunique() != 39:
        raise RuntimeError(f"{cohort}: expected 39 paired rows/components")

    y = x["label"].to_numpy(float)
    native = x["native_prediction"].to_numpy(float)
    candidate = x["candidate_prediction"].to_numpy(float)

    native_m = basic_metrics(y, native)
    candidate_m = basic_metrics(y, candidate)

    native_log = np.abs(np.log1p(native) - np.log1p(y))
    candidate_log = np.abs(np.log1p(candidate) - np.log1p(y))
    paired_delta = candidate_log - native_log

    # Whole-component percentile bootstrap. Each released primary paired cohort
    # contains one row per source component, so component resampling is row
    # resampling here. Seeds are the frozen manuscript seeds.
    rng = np.random.default_rng(bootstrap_seed)
    n = len(paired_delta)
    idx = rng.integers(0, n, size=(5000, n))
    draws = np.mean(paired_delta[idx], axis=1)
    ci_low, ci_high = np.quantile(draws, [0.025, 0.975])

    reduction = 100.0 * (native_m["macro_log1p"] - candidate_m["macro_log1p"]) / native_m["macro_log1p"]
    improved = int(np.sum(candidate_log < native_log))

    print(f"\n{cohort} primary endpoint")
    print("native:", native_m)
    print("candidate:", candidate_m)
    print(f"candidate-native macro log1p delta: {paired_delta.mean():.12f}")
    print(f"saved-style 95% percentile interval: [{ci_low:.12f}, {ci_high:.12f}]")
    print(f"primary-loss reduction: {reduction:.6f}%")
    print(f"lower candidate error: {improved}/{n}")


def external83(df):
    if len(df) != 83 or df["source_component"].nunique() != 83:
        raise RuntimeError("External83: expected 83 rows/components")

    print("\nExternal83 original frozen evaluation")
    print("Area:", basic_metrics(df["area_label_um2"], df["area_prediction_um2"]))
    print("Timing:", basic_metrics(df["timing_tmin_label_ns"], df["timing_prediction_ns"]))

    p = df.loc[df["top_module_label"].eq("pipelineTop")]
    if len(p) != 1:
        raise RuntimeError("Expected exactly one pipelineTop row")
    row = p.iloc[0]
    print(
        "pipelineTop:",
        f"measured Tmin={row['timing_tmin_label_ns']:.12f} ns,",
        f"prediction={row['timing_prediction_ns']:.12f} ns",
    )

    without = df.loc[~df["top_module_label"].eq("pipelineTop")]
    timing_wo = basic_metrics(without["timing_tmin_label_ns"], without["timing_prediction_ns"])
    print("Timing without pipelineTop (post-hoc sensitivity only):", timing_wo)


def main():
    fresh = pd.read_csv(FRESH)
    external = pd.read_csv(EXTERNAL)

    fresh_endpoint(fresh, "Reserve50", bootstrap_seed=143)
    fresh_endpoint(fresh, "Source50", bootstrap_seed=149)
    external83(external)


if __name__ == "__main__":
    main()
