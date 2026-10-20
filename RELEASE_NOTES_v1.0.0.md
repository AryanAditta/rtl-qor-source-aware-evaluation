# v1.0.0 – Manuscript Reproducibility Release

This is the submission-oriented archival release accompanying the manuscript:

**Source-Aware Evaluation of RTL Area and Timing Prediction with Prospective Confirmation**

## Scope

This release contains the compact, frozen evidence required to inspect the manuscript's reported results without mirroring the full historical Google Drive archive.

Included material covers:

- frozen R4.1 closure and manuscript-claim records;
- M12 field-comparable metric tables and metric policy;
- M13 development-only TimingV2 family ablation records;
- M14 MasterRTL-method adaptation gate and fidelity-boundary records;
- prediction-level data for the original External83 evaluation;
- the 39 paired Reserve50 Area prospective-confirmation cases;
- the 39 paired Source50 Timing prospective-confirmation cases;
- secondary Source50 Area paired predictions;
- scripts for recomputing the released primary prediction-level metrics;
- reproducibility, provenance and third-party redistribution documentation.

## Important boundaries

This release does not include the full research archive, 100+ historical notebooks, large source-artifact indexes, redundant checkpoints, private/supervisor files or third-party RTL whose redistribution rights are uncertain.

The MasterRTL Timing adaptation stopped at the frozen path-correspondence gate before any path learner was fitted. This release therefore contains no MasterRTL Timing accuracy comparison and makes no claim that the published method is inaccurate or intrinsically unreproducible.

The evidence was frozen at R4.1. No new model fitting, feature selection, target relabelling, STA campaign or post-freeze result-driven model selection is part of this release.

## Licensing

- Repository-authored source code: MIT License (`LICENSE`).
- Repository-authored data tables, prediction records, result tables, metadata and documentation: CC BY 4.0 (`LICENSE-DATA.md`).
- Third-party materials remain governed by their upstream licenses and are not relicensed by this repository.

## Citation

`CITATION.cff` provides repository citation metadata. A version-specific Zenodo DOI should be associated with this exact `v1.0.0` release and then added to the manuscript's Data and Code Availability statement.
