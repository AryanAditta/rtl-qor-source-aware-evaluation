# Released prediction-level data

This directory contains compact manuscript-facing tables derived from the frozen project evidence. It intentionally does not contain the full source archive or the complete historical Drive tree.

## Files

### `cohort_support_summary.csv`
Records the intended, prediction-supported, valid-label and paired counts used in the manuscript for External83, Reserve50 and Source50. These are separate set counts; Reserve50 and Source50 must not be interpreted as sequential funnels.

### `fresh_primary_predictions.csv`
Contains the two method-specific prospective paired comparisons:

- Reserve50 Area: 39 paired rows/components
- Source50 TimingV2: 39 paired rows/components

Columns retain only the source/component identifier, measured target, frozen native prediction, frozen candidate/system prediction and unit. These values reproduce the primary MAE, RMSE, component-macro absolute log1p loss, 27/39 improvement counts and saved paired bootstrap contrasts reported in the manuscript.

### `source50_secondary_area_predictions.csv`
Contains the secondary Source50 Area comparison on the same 39 Source50 paired designs. It is not another independent acquisition cohort. The candidate improves mean losses while MdAPE is slightly worse than the native comparator; this metric reversal is intentionally preserved.

### `external83_primary_predictions.csv`
Contains all 83 original frozen external cases for both Area and Timing. The influential `pipelineTop` case is retained. The file omits repository paths and other unnecessary acquisition metadata while preserving the identifiers, top-module label, measured targets and frozen predictions needed to reproduce the manuscript's External83 metrics and the named post-hoc sensitivity.

## Provenance

These compact tables were assembled from the frozen closure inputs without refitting models, changing labels, rerunning synthesis/STA or recomputing model predictions. They are release views of the saved evidence, not new experimental cohorts.

The full raw source/configuration archive is deliberately not published here because this manuscript package is scoped to claim checking and because some upstream RTL/dependencies may carry third-party redistribution restrictions.
