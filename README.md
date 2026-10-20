# Source-Aware RTL Area and Timing Prediction

Curated reproducibility package for the manuscript **“Source-Aware Evaluation of RTL Area and Timing Prediction with Prospective Confirmation.”**

This repository supports a study of early RTL prediction for two targets under one pinned open-source Nangate45 flow:

- **Mapped standard-cell area** in µm²
- **Standardized pre-layout minimum feasible clock period (`Tmin`)** in ns

The repository is intentionally **not** a mirror of the full research drive or historical notebook archive. It contains only the compact artifacts needed to inspect the manuscript’s frozen evidence, cohort chronology, reported comparisons and reproducibility boundaries.

## Evidence status

The scientific evidence was frozen at **R4.1** on 17 October 2026. The closure record states that manuscript writing is the next step and that there is **no M15** or further model/cohort/STA campaign for this manuscript.

The development corpus contains **681 labelled configurations in 498 source-connected components**. A configuration is not necessarily an independent design.

The two principal prospective confirmations are method-specific:

- **Reserve50 Area:** 50 intended inputs, 47 prediction-supported, 40 validly labelled and **39 paired**. The frozen graph-primary Area system reduced MAE from approximately **8,382 to 3,015 µm²** and component-macro absolute log1p error by **58.9%** relative to its frozen native comparator on the paired evaluable intersection.
- **Source50 Timing:** 50 intended inputs, 41 prediction-supported, 45 validly labelled and **39 paired**. The frozen TimingV2 candidate reduced MAE from approximately **0.167 to 0.136 ns** and the primary component-macro absolute log1p loss by **17.5%** relative to its frozen native comparator on the paired evaluable intersection.

These results are conditional on prediction support and valid physical labels. They do not establish post-layout/signoff accuracy, cross-technology transfer, arbitrary-RTL support or a state-of-the-art ranking across incompatible published targets.

## Repository scope

The release is organized around four layers:

```text
admin/            frozen protocols, closure/freeze records and claim registry
results/          compact manuscript-supporting tables and prediction-level outputs
analysis/         selected final analysis notebooks/scripts required to reproduce reported tables/figures
reproducibility/  environment, manifests, provenance notes and release boundaries
docs/             detailed reproduction and data-availability notes
```

Large historical inventories, redundant intermediate checkpoints, debugging artifacts, private/supervisor material and third-party RTL that cannot be redistributed are deliberately excluded.

## Predictor identities

The manuscript distinguishes several source-derived representations rather than treating them as one model:

- `Area56`: generic RTLIL area-oriented structural descriptors
- `Timing74`: source-derived timing/connectivity structural descriptors
- `Graph14`: a 14-dimensional feature vector derived from an adapted MasterRTL Area operator graph; **not a GNN and not the published MasterRTL Timing method**
- `TimingV2`: 39 additional source-derived structural burden aggregates used with Timing74

ExtraTrees regressors are used for the retained native, graph-derived and TimingV2 recipes. Physical labels are generated separately through the pinned Yosys/ABC/OpenSTA flow; mapped netlists and timing labels are not predictor inputs at inference.

## Important evaluation boundaries

- Related RTL configurations are grouped through recorded source-component relationships for grouped evaluation.
- Freshness is assigned to a **method/cohort prediction freeze**, not permanently to a dataset.
- The original External83 test keeps all 83 valid cases, including the influential `pipelineTop` Timing case.
- Fresh Area fallback accuracy is **not** established because no Reserve50 native-route case was both prediction-supported and validly labelled.
- The assessed MasterRTL Timing adaptation stopped before fitting because no bridge-valid design met the frozen 95% usable path-record correspondence gate; therefore this repository does **not** claim a MasterRTL Timing accuracy comparison.
- Prediction-interval coverage is reported as cohort evidence, not as a universal coverage guarantee.

## Reproducibility levels

This repository distinguishes three different goals:

1. **Prediction-level checking** — verify saved predictions, labels, cohort membership and manuscript metrics.
2. **Model retraining** — reproduce retained model recipes where redistributable inputs are available.
3. **Physical-label regeneration** — requires the pinned synthesis/STA toolchain and source dependencies and may not be fully reproducible from this public repository alone.

See `docs/REPRODUCIBILITY.md` and `reproducibility/RELEASE_MANIFEST.md` for the exact included/excluded scope.

## Manuscript, citation and archival release

The manuscript is currently in submission preparation for *Integration, the VLSI Journal*.

The submission-oriented archival release is designated **v1.0.0**. `CITATION.cff` contains repository citation metadata. After the GitHub repository is connected to Zenodo and the v1.0.0 release is archived, the **version-specific Zenodo DOI** will be added here and to the manuscript Data and Code Availability statement.

## Licensing

This repository uses a split licensing model:

- **Source code:** MIT License, see `LICENSE`.
- **Original data tables, prediction records, result tables, metadata and documentation:** Creative Commons Attribution 4.0 International (**CC BY 4.0**), see `LICENSE-DATA.md`.
- **Third-party material:** not relicensed. External RTL, software, libraries and published methods remain governed by their respective upstream licenses and terms.

The public package intentionally avoids redistributing third-party RTL unless redistribution permission is clear. See `reproducibility/THIRD_PARTY_NOTICE.md` for details.
