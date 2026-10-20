# M12 metric policy

Protocol SHA-256: 168023aaa7a31a2d5d6f8014245a19e7feed4e17ad2dc1c39225148e34464506

### 0.4 Shared metric definitions
Let *y* be the measured target, *ŷ* the frozen or out-of-fold prediction, and *n* the number of paired rows. All computations use unrounded values; displays round to 4 significant figures.

| Metric | Definition | Notes |
|---|---|---|
| MAE | mean \|ŷ − y\| | Target units (µm² or ns) |
| RMSE | sqrt(mean (ŷ − y)²) | Target units |
| Raw R² | 1 − SSE/SST on raw values | Not squared Pearson |
| Pearson r | Pearson correlation of (y, ŷ), raw scale | Field-comparable with MasterRTL/RTL-Timer |
| Spearman ρ | Rank correlation of (y, ŷ) | |
| ln R² | 1 − SSE/SST on (ln y, ln ŷ) | Rows with y ≤ 0 or ŷ ≤ 0 excluded and **counted** |
| Row log error | mean \|ln(1+ŷ) − ln(1+y)\| | |
| Macro log error | mean over source components of the component-mean \|ln(1+ŷ) − ln(1+y)\| | The project's primary component-equal metric |
| Raw MAPE | mean (\|ŷ − y\| / y) × 100 over y > 0 | Unstable when y is tiny (Tmin down to ~0.004 ns); always shown with a warning |
| MdAPE | median (\|ŷ − y\| / y) × 100 over y > 0 | Robust companion to MAPE |
| Capped MAPE | mean min(APE, 100%) | Labelled **"MasterRTL-compatible capped MAPE"**, secondary only. MasterRTL capped per-design APE above 100% at 100% |
| Within ±10% / ±20% | share of rows with \|ŷ − y\| ≤ 0.10·y (resp. 0.20·y), boundary inclusive, y > 0 | Report counts and denominators |

---

## 1. M12 — Field-comparable metrics from frozen predictions

### 1.1 Question
How do the already-frozen predictions look under the metrics other RTL-QoR papers report, without changing any prediction?

### 1.2 Evidence role
`DESCRIPTIVE_FROZEN_PREDICTIONS`. No fitting, no inference, no resampling.

### 1.3 Eligible predictor/cohort pairs (exhaustive list, fixed now)

| ID | Cohort | Predictor(s) | Target(s) | Expected source |
|---|---|---|---|---|
| P1 | Full681 grouped OOF | Stage79 source-component native reference (Area56 ET-sqrt; Full231 ET-log) | Area, Tmin | Stage79 run folder (per-design OOF file) |
| P2 | External83 | Original Stage69 frozen native | Area, Tmin | `stage70_prelabel_predictions.csv` + Stage71 labels (`external83_points.csv` in R1 evidence) |
| P3 | Reserve50 paired | Frozen graph-primary hybrid; frozen native | Area (primary); Tmin (system = native) | `reserve_predictions.csv`, `reserve_evaluation.csv`, `reserve_labels.csv`; native per-design Area predictions from Stage143/144 |
| P4 | Source50 paired | Frozen native Timing reference; frozen Timing74+V2 candidate. Secondary: hybrid vs native Area | Tmin (primary); Area (secondary) | Stage150/151R run folders |
| P5 | Proper538 broad OOF | Stage146 REFERENCE (Full231), T74_ONLY, T74_V2, FULL231_V2 | Tmin | `broad_oof.csv` (M05 source evidence) |
| P6 | Common support 168/166 | M05 Full231, Graph14, Timing74, Timing74_V2 | Tmin | `M05_COMMON_SUPPORT_OOF_PREDICTIONS.csv` |

Not eligible: size controls, Historical452, Matched204, External83 later baselines, Phase45 OOF (a different model identity). These either have stored aggregate metrics only or are not manuscript primary results.

### 1.4 Inventory audit (runs before any metric)
For each pair, report: expected rows → unique design IDs → source components → prediction rows found → label rows found → paired eligible rows → rows with y ≤ 0 or ŷ ≤ 0.

- **Expected counts (must match, or the pair is flagged):** P1 681/498; P2 83/83; P3 39/39 paired; P4 39/39 paired; P5 538/398; P6 168/166 per representation.
- **If a pair has no per-design prediction file, it is reported as `NOT_AVAILABLE_PER_DESIGN`, and its stored aggregate metrics from R3_2 are referenced unchanged.** It is never reconstructed by refitting.
- Join keys and any ID normalisation are written into the run record.

### 1.5 Computation
- All §0.4 metrics, for every eligible pair and target, in one table. No metric is omitted for any pair.
- External83 Timing: the primary row includes all 83 designs. A second row "without pipelineTop" is shown **only** as the already-disclosed S13 post-hoc sensitivity, labelled as such.
- Units: Area in µm², Tmin in ns.

### 1.6 Outputs
- `M12_INPUT_INVENTORY.csv`
- `M12_Table_Peer_Comparable_Metrics.csv` (all pairs × all metrics)
- `M12_Table_External83_Error_Regimes.csv` (error by measured-target tercile: small/medium/large designs, counts shown)
- `M12_METRIC_POLICY.md` (definitions, the MAPE warning, the capped-MAPE label)
- `M12_CONSISTENCY_CHECKS.csv`: recomputed MAE, RMSE, raw R², Spearman and macro log error are compared **only against the machine-readable, unrounded R3_2 source value** for the same pair (for example the `*_raw.csv` table files or ledger values), within 1e-9 relative. Any mismatch → **FAIL**, stop, investigate, do not adjust. If no machine-readable unrounded reference exists for a pair, its status is `NOT_CHECKABLE_EXACT`. **The tolerance is never loosened to force a match**, and rendered or rounded manuscript numbers are never used as the reference.

### 1.7 Manuscript use
These numbers go into one main-paper "field-comparable metrics" table. The R3_2 primary metrics remain primary.

---



Implementation conventions: CSV numeric tokens are parsed with Python float(), without rounded display intermediates. No ID normalization. Undefined correlations/R² (constant or insufficient population) are blank, with reason/count fields. No epsilon is inserted into MAPE denominators. Shares are in [0,1]; APE statistics are percentages. Log1p-invalid values stop analysis, with no clipping. Terciles use linear target quantiles; ties remain together and empty regimes are reported. Natural-log R² is ln(y), not ln(1+y). Capped MAPE is secondary only. Missing per-design inputs never trigger reconstruction. Relative consistency tolerance is 1e-9 with zero absolute tolerance.
