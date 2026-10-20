# Reproducibility scope

This repository is a curated manuscript-support package. It is not the complete historical research archive.

## What this release is intended to support

### 1. Prediction-level checking

The primary public reproducibility target is verification of saved prediction-level evidence:

- cohort and support counts;
- measured Area and `Tmin` values where redistribution is permitted;
- frozen native, Area-system and TimingV2 predictions;
- component-aware metric calculations;
- External83 descriptive analyses;
- M13 development-only TimingV2 family ablation;
- M14 feasibility/adaptation-gate outcome;
- final R4.1 evidence-freeze records.

A reviewer should be able to recompute the reported manuscript metrics from the released compact tables without rerunning synthesis or STA.

### 2. Analysis-code inspection

Selected final closure scripts/notebooks are included where they directly generate or audit manuscript-facing results. Historical notebooks that were superseded, exploratory, redundant or used only for debugging are excluded.

### 3. Model retraining

Retraining is a secondary reproducibility level. Retained recipes and feature definitions are documented, but full retraining may depend on source material or intermediate representations that cannot be redistributed. The public package therefore does not claim that every historical model can be regenerated from a clean checkout.

### 4. Physical-label regeneration

The Area and Timing targets were produced through a pinned open-source synthesis/STA contract based on Yosys/ABC, OpenSTA and the Nangate45 typical Liberty library. Recreating labels also requires each design's source/configuration/dependency closure and the project-specific acceptance contract.

Because some source material is third-party and may have redistribution restrictions, this public repository does **not** claim complete end-to-end label regeneration for every row.

## Frozen scientific boundary

The final evidence freeze is **R4.1**. Its closure record states:

`MANUSCRIPT_WRITING_ONLY;NO_M15;FUTURE_IDEAS_LOGGED`

M12, M13 and M14 were preregistered as the final three analysis notebooks for the manuscript. R4/R4.1 close the evidence after those analyses.

## Cohort chronology

Freshness is method-specific rather than an intrinsic property of a dataset.

- **External83:** original blind test for the original native models; later reuse is retrospective.
- **Reserve50:** prospective confirmation for the frozen Area system. It is retrospective for TimingV2.
- **Source50:** prospective confirmation for the frozen TimingV2 candidate; its Area comparison is secondary.
- **Historical452:** repaired historical evidence and not an independent fresh confirmation for later methods.

For Reserve50 and Source50, intended inputs, prediction-supported inputs, valid labels and paired evaluable cases are separate sets and must not be represented as one sequential funnel.

## Target definitions

- **Area:** mapped standard-cell area in µm² under the stated Nangate45 mapping contract. It is not die area, routed area or placement area.
- **`Tmin`:** the smallest feasible clock period found by the recorded bounded pre-layout OpenSTA search. It is not post-route or signoff timing.

## Main representation boundaries

- `Graph14` is a 14-dimensional feature vector derived from an adapted MasterRTL **Area** operator graph. It is not a GNN and does not reproduce the published MasterRTL Timing predictor.
- `TimingV2` is a 39-feature source-derived structural augmentation used with Timing74. It is not a learned timing graph or path predictor.
- The assessed MasterRTL Timing adaptation stopped at the frozen path-correspondence gate and produced **no accuracy comparison**.

## Files deliberately excluded

The following classes are not part of the public package unless a later author-approved release explicitly adds them:

- the ~298 MB historical source-artifact index;
- the full Google Drive archive and 100+ historical notebooks;
- superseded checkpoints and result bundles;
- intermediate debug files;
- private/supervisor documents;
- source RTL or dependencies without clear redistribution permission;
- the ~276 MB M14 diagnostic bundle, whose manuscript-facing gate summaries are released separately;
- unrelated project material.

## Integrity

The public release preserves original final-closure filenames where useful and records the R4.1 freeze/bundle hashes. A later archival release should be versioned and assigned a persistent DOI. GitHub remains the readable development/review surface; an archival service such as Zenodo can freeze the submission version.
