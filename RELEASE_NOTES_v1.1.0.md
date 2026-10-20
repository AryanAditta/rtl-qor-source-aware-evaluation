# v1.1.0 – Manuscript Reproducibility Update

This release extends the submission-oriented reproducibility package for the manuscript **“Source-Aware Evaluation of RTL Area and Timing Prediction with Prospective Confirmation.”**

## Added in v1.1.0

- `posthoc_analysis/posthoc.py` — post-hoc robustness analysis on the frozen per-design predictions; no model fitting, recalibration or reselection.
- `posthoc_analysis/make_figs.py` — revised manuscript figure-generation code based on frozen data/tables.
- `posthoc_analysis/PH1_log_ratio_contrasts.csv` — absolute log-ratio sensitivity results for the fresh paired comparisons.
- `posthoc_analysis/PH2_relative_interval_widths.csv` — relative prediction-interval width and coverage summaries.
- `posthoc_analysis/PH3_absolute_error_contrasts.csv` — paired absolute-error contrasts in physical units.

## Scientific boundary

The added analyses are explicitly post hoc. They re-score frozen predictions and frozen intervals after all fresh labels were known. They do **not** refit a predictor, alter a label, change cohort membership, recalibrate intervals or reselect a model. The original prospective primary endpoints and their frozen conclusions remain unchanged.

The Area conclusion remains robust under the added error metrics. The Timing result remains favorable under the prespecified primary loss and in physical-unit MAE, while the post-hoc absolute log-ratio interval includes zero; this metric sensitivity is reported in the revised manuscript.

## Existing release boundaries

The repository still does not include the full historical research archive, redundant intermediate checkpoints, private/supervisor material or third-party RTL whose redistribution rights are uncertain. The MasterRTL Timing adaptation still stops at the frozen path-correspondence gate before any timing-path learner is fitted, so no MasterRTL Timing accuracy comparison is claimed.

## Licensing

- Repository-authored source code: MIT License (`LICENSE`).
- Repository-authored data tables, prediction records, result tables, metadata and documentation: CC BY 4.0 (`LICENSE-DATA.md`).
- Third-party materials remain governed by their upstream licenses and are not relicensed by this repository.
