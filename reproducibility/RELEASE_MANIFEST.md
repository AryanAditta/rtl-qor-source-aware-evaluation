# Public release manifest

This manifest defines the intended manuscript-submission package. It is deliberately smaller than the research Drive.

## Include

### Administrative / frozen evidence
- R4.1 freeze and decision records
- R4.1 claim/boundary registry
- M12–M14 preregistered protocol
- compact R4.1 integrity/check records

### Prediction-level evidence
- Full681 grouped OOF prediction/identity tables needed for manuscript metrics
- External83 prediction/label points
- Reserve50 paired Area prediction/label tables
- Source50 paired Timing and secondary Area prediction/label tables
- Proper538/common-support OOF tables used by M12/M13
- source-component group assignments used by the retained grouped evaluation

### Manuscript-facing analyses
- M12 peer-comparable metric table, consistency checks, input inventory, metric policy and External83 regime table
- M13 family definitions, ablation metrics, paired deltas, seed-noise record and interpretation
- M14 gate/coverage/audit/diagnostic summaries and final decision
- selected final analysis code/notebooks required to inspect or reproduce these tables

### Documentation
- repository README
- reproducibility scope
- third-party/redistribution notice
- final environment/provenance notes where available

## Exclude

- complete Google Drive hierarchy
- `SOURCE_ARTIFACT_INDEX.csv` (~298 MB)
- historical stage folders and redundant notebooks
- superseded evidence ledgers when the R4.1 form is available
- intermediate checkpoints/debug artifacts
- the full M14 diagnostic result bundle (~276 MB)
- private or supervisor-only material
- third-party RTL/dependency files without confirmed redistribution permission
- unrelated research projects

## Release rule

A file is public only if it is needed to verify a manuscript claim, understand the evaluated population/chronology, inspect the final analysis procedure or reproduce a reported figure/table **and** it is safe to redistribute.

The release should remain compact enough for a reviewer to understand without reconstructing the historical Drive workflow.
