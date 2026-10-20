# R4 Preregistered Protocols: M12, M13, M14

**Project:** RTL-to-QoR prediction — manuscript closure
**Parent evidence freeze:** R3_2 (`R3_2_20261015T202511_138415Z_RESULT_BUNDLE.zip`, 3,296/3,296 checks PASS)
**Version:** v1.1, which includes six review revisions made before the file was first hashed: the M12 reference rule, the M13 seed-noise and reproducibility definitions, the M14 bridge tolerance, component-level gates, path-record correspondence, and training-support disclosure.
**Status of this document:** FROZEN BEFORE EXECUTION. Record its SHA-256 in every M12–M14 run record before any analysis cell runs. Any later change requires a dated amendment section at the end of this file. Do not edit earlier text.

---

## 0. Rules that apply to all three notebooks

### 0.1 Scope
- These are the **last three notebooks for this manuscript**. After them, one append-only freeze (**R4**) is issued, referencing R3_2. **There is no M15.**
- R3_2 and every earlier record stay unchanged. M12–M14 outputs are new, appended records.
- Fresh-confirmation status stays where it is: Reserve50 is fresh only for the frozen Area system, and Source50 only for the frozen TimingV2 candidate. Nothing in M12–M14 creates new "fresh" evidence.

### 0.2 Execution conventions (same as the M-series)
- Drive root: `/content/drive/MyDrive/RTL_QOR_DATASET_V2`. `06_v3_dataset` is read-only.
- Outputs go to `07_manuscript_closure/03_results/audits/<RUN_ID>/`. `RUN_ID = <Mxx>_<UTC timestamp>`.
- **Cell 1 of every notebook:** mount Drive, list every input file, compute and record SHA-256, row counts and column lists **before any content is analysed**. Input paths in this document are placeholders until that cell resolves them. The notebook records the real hashes; never type hashes in by hand.
- **Cell 2:** record this protocol file's SHA-256 and the run environment (Python, NumPy, SciPy, pandas, scikit-learn versions).
- Ledger write-back: guarded append to `07_manuscript_closure/00_admin/EVIDENCE_LEDGER.csv`, with a backup copy and a conflict check, as in M02–M11.
- Every output table carries an `evidence_role` column. The allowed values for M12–M14 are `DESCRIPTIVE_FROZEN_PREDICTIONS`, `DEVELOPMENT_ABLATION`, `RETROSPECTIVE_ADAPTED_BASELINE` and `FEASIBILITY_AUDIT`.
- A result bundle ZIP is written at the end. A notebook that fails a gate still writes its bundle, with the failure recorded.

### 0.3 Forbidden in all three notebooks
- Changing, deleting or re-deriving any stored target label (Area, Tmin), or deleting any design from a primary population after seeing results. pipelineTop stays in.
- Changing the frozen TimingV2 candidate, the frozen Area system or any frozen prediction file.
- Hyperparameter search, feature selection, threshold tuning or metric selection based on results.
- Using Source50, Reserve50 or External83 to select or adjust anything.
- Adding cohorts, technology libraries, post-layout targets, power targets, or neural/LLM models.
- Reporting only a favourable subset of the metrics declared here.

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

## 2. M13 — Descriptive TimingV2 family ablation

### 2.1 Question
Within development data only, how much does each predefined TimingV2 feature family contribute to Tmin prediction?

### 2.2 Evidence role
`DEVELOPMENT_ABLATION`. Descriptive only. **Whatever the result, the frozen TimingV2 candidate is not changed, and no "TimingV3" is created for this manuscript.**

### 2.3 Population and folds
- Proper538 (538 rows / 398 source components) only.
- Inherited source-component outer folds from the M05/Stage146 split file (`split.csv`), unchanged.
- InternalCal143, Reserve50, Source50 and External83 are not loaded for fitting or evaluation.

### 2.4 Families (fixed now, from M06; the counts must match)
Families come from the M06 frozen table `Table_TimingV2_Feature_Definitions.csv`, column `family`. Hash that table in Cell 1.

| # | Family | Features |
|---|---|---|
| F1 | Operator widths | 8 |
| F2 | Chain and width interaction | 7 |
| F3 | Depth and topology | 5 |
| F4 | Structural density | 4 |
| F5 | Memory structure | 2 |
| F6 | Endpoint and interface | 4 |
| F7 | Clock control and design type | 6 |
| F8 | Connectivity diagnostics | 3 |
| | **Total** | **39** |

If the M06 table's family assignment differs from these counts, **stop** and record the discrepancy. Do not re-assign features.

### 2.5 Configurations (exactly 10)
1. `T74`: Timing74 only (74 features)
2. `T74_V2_FULL`: Timing74 + all 39 (113 features), the frozen candidate representation
3–10. `T74_V2_minus_Fk` for k = 1…8: the full set minus family k

Removing a family removes only its derived TimingV2 columns, never raw Timing74 or Area56 columns.

### 2.6 Learner (fixed)
- **Reference run:** the Proper538 broad-population results come from **Stage146** (stored out-of-fold predictions in `broad_oof.csv`). M05 refit models only on the 168-row common-support subset and reused the Stage146 broad predictions without refitting. M13 therefore uses the **Stage146 T74_V2 recipe** (ExtraTrees configuration, target transform, seed, and inverse transform), read from the Stage146 protocol/package files (`stage146_protocol.json`, `frozen_timing_v2.py`, `timing_candidate_package.json`) and recorded verbatim. Cell 1 cross-checks it against the M05 fit log; any difference is recorded, and the Stage146 recipe governs. All 10 configurations use it.
- Primary seed: the recorded Stage146 seed, s₀.
- **Extra seeds (deterministic rule):** the first five integers in {1, …, 10} that are not equal to s₀.
- **Seed noise floor (defined exactly):** let E₀ be the macro log error of `T74_V2_FULL` at s₀, and E_s its macro log error at each extra seed s. Then **N_seed = max_s |E_s − E₀|**.

### 2.7 Metrics and comparisons
- All §0.4 metrics for each configuration, from out-of-fold predictions.
- Primary comparison: macro log error of each `minus_Fk` vs `T74_V2_FULL`, as paired per-component differences, with a descriptive component bootstrap (5,000 resamples, seed 20261017). No p-values, no significance language.
- **Reproducibility check (separate from seed noise):** at seed s₀, `T74_V2_FULL` and `T74` are compared with the stored Stage146 broad-population macro log errors (0.122494 and 0.145878, using the unrounded values from `broad_oof.csv`). Same seed, folds and recipe should reproduce the stored run:
  - If the library versions match Stage146: pass requires a relative difference ≤ 1e-6. Otherwise **FAIL**: stop and investigate before any ablation is interpreted.
  - If the library versions differ: status `ENVIRONMENT_DIFFERENT`. Record the versions and the exact difference. The ablation still runs, but every comparison is made **within the M13 run only** (each `minus_Fk` against M13's own `T74_V2_FULL` at s₀), and the manuscript reports the difference from Stage146.
  - The seed noise floor is never used as the tolerance for this check.

### 2.8 Interpretation rules (fixed now)
- A family is reported as **"within seed noise"** when |E₋Fk − E₀| ≤ N_seed, where E₋Fk is the macro log error of `T74_V2_minus_Fk` at s₀. It is never described as "irrelevant".
- A small effect does **not** imply a family is unimportant, because correlated families can substitute for one another. This sentence appears in the output.
- F5 (2 features) and F6 (4 features) are expected to be noisy. Their results are reported but carry no individual claims.
- If removing a family *improves* development error, this is reported as a descriptive finding only. It does not license a new candidate.

### 2.9 Outputs
`M13_FAMILY_DEFINITIONS.csv`, `M13_ABLATION_METRICS.csv`, `M13_PAIRED_DELTAS.csv`, `M13_SEED_NOISE.csv`, `M13_Fig_TimingV2_Ablation.pdf`, `M13_ABLATION_INTERPRETATION.md`.

---

## 3. M14 — Adapted MasterRTL Timing baseline

### 3.1 Question
Under this project's Tmin target and pinned flow, on the same source-grouped population, how does an adaptation of the released MasterRTL timing method compare with the representations evaluated in M05?

### 3.2 Naming (fixed)
Always: **"MasterRTL-method adaptation under our timing-label contract."** Never "MasterRTL reproduction" or "MasterRTL Timing reproduced."

### 3.3 Evidence role
`FEASIBILITY_AUDIT` (Gates 1–3), then `RETROSPECTIVE_ADAPTED_BASELINE` (Gate 4).

### 3.4 Hard time box
**7 calendar days from the first Gate 1 cell execution.** The start timestamp is written to the run record. Debugging does not extend the deadline. At the deadline, whatever gate is incomplete is recorded as the fidelity boundary, and M14 closes.

### 3.5 Population
- Primary: the M05 common graph-supported population, 168 rows / 166 components, with the inherited M05 outer folds.
- External83, Reserve50 and Source50 are **not part of M14**.

### 3.6 Gate 1 — Released-method audit
Record:
- Repository and commit (expected `f78bcf1b777d8e694078a1cdd7b692147bb7ffb6`, as used for Graph14).
- The files implementing timing-path feature extraction, path labelling, the path learner and design-level WNS/TNS aggregation.
- Learner configuration as released (recorded expectation: RandomForest, 50 trees, max depth 30, seed 1). Verify it in code; do not assume it.
- Each required input classified as PUBLIC, RECONSTRUCTABLE from our flow, or PRIVATE (expected private: `feat_all_lst.pkl`, `label_lst.pkl`).

**Pass:** all non-private inputs are either present or reconstructable, and the aggregation from path predictions to a design-level worst slack is identifiable in code.

### 3.7 Gate 2 — Timing-contract bridge
Target bridge: **T̂min = T_ref − worst_slack(T_ref)**, with T_ref = 0.2 ns. Use the **unclipped worst slack**, never WNS (WNS is clipped at 0).

- Path-level STA runs for M14 use the existing mapped netlists, the pinned OpenSTA binary and Liberty file, and the same clock/IO constraint template as the stored Tmin search, with the period fixed at 0.2 ns. These runs generate supervision for the adapted method only. **Stored Tmin labels are never replaced.**
- For **every** design in the 168-row population, compute the residual r = \|0.2 − worst_slack₀.₂ − Tmin_stored\|. For External83, the stored `worst_slack_0p20_ns` column is also checked as a cross-validation of the bridge; no M14 model touches External83.
- Tolerance (fixed): a design is bridge-valid if **r ≤ max(0.001·Tmin_stored, 0.001 ns)**, i.e. 0.1% or 1 ps, whichever is larger. This is consistent with the stored Tmin search (period tolerance 1e-4 ns). The STA runs must use the same hash-verified OpenSTA binary and Liberty file as the stored labels; a hash mismatch fails Gate 2.
- Exceptions characterised before any model result: negative-edge or half-cycle capture, multiple clocks, critical path in an asynchronous (recovery/removal) group, combinational virtual-clock designs. Each failing design gets its reason code.
- **Exclusion rule:** a design is excluded from Gate 4 **only** for failing the bridge, with its reason. MasterRTL prediction accuracy is never inspected when deciding exclusions. All exclusions go in `M14_BRIDGE_EXCLUSIONS.csv`.

**Pass:** ≥ 80% of rows **and** ≥ 80% of source components are bridge-valid, i.e. at least **135/168 rows and 133/166 components**. These are **engineering feasibility thresholds, not statistical criteria**.

### 3.8 Gate 3 — Path-record correspondence
- Map the sequential objects that the released MasterRTL path extractor requires (launch and capture registers, and any other endpoint or path identities it uses) to instances in the mapped netlist. The mapping rule (name normalisation steps) is written down before mapping and recorded.
- **Primary metric, per design:** the percentage of selected top-1% STA path records for which **every sequential identity required by the released extractor** maps deterministically to the graph. **A design passes if ≥ 95% of its path records are fully usable.**
- **Diagnostic only:** unique-register match rate, reported but never used as a gate.
- **Gate pass:** ≥ 80% of bridge-valid rows **and** ≥ 80% of bridge-valid components pass per-design (engineering feasibility thresholds).
- Designs failing correspondence are excluded from Gate 4 with reason code `PATH_RECORD_MAPPING`. This is never decided by looking at accuracy.
- Expected risk: earlier public path-supervision work in this project admitted only 13 components, so Gate 3 is the most likely point of failure. A Gate 3 failure is a legitimate, reportable fidelity boundary.

### 3.9 Pre-committed interpretation (frozen now, before Gate 4)

| Outcome | What the manuscript says |
|---|---|
| Adapted MasterRTL has lower error | Report it plainly: the evaluation framework shows a stronger published method transfers under this contract |
| TimingV2 has lower error | "Under this same-flow Tmin adaptation, TimingV2 had lower error." Never "beats MasterRTL" |
| Mixed (different metrics favour different methods) | Report the metric-specific trade-off, as M05 did for Graph14 |
| Any gate fails or the time box expires | Report the exact fidelity boundary (which gate, which step, how many designs). No baseline numbers |

Under every outcome there is no hyperparameter search, no re-specification of the adaptation, and no rerun "to check".

### 3.10 Gate 4 — Fixed baseline evaluation (only if Gates 1–3 pass)
- Train the adapted path learner with the released configuration on training-fold paths of the inherited M05 folds; predict held-out designs; aggregate to design-level worst slack as the released code does; convert with the Gate 2 bridge.
- **Evaluation set:** the intersection of bridge-valid and correspondence-valid rows ("M14 intersection").
- Comparators on the same intersection rows: M05 OOF predictions for Full231, Graph14, Timing74 and Timing74_V2, restricted to those rows. These are **not refit**. Note in the output that they were trained on all 168 rows.
- All §0.4 metrics, plus paired per-component macro-log differences (adapted MasterRTL − each comparator), with a descriptive component bootstrap (5,000 resamples, seed 20261017).
- **Coverage table:** 168 → bridge-valid → correspondence-valid → evaluated, in rows and components, with reason codes. Coverage is reported next to accuracy, so a narrow subset never appears to dominate a broader method.
- **Training-support table, per fold:** `train_rows_available`, `train_components_available` and `heldout_rows_evaluated` for the adapted method, alongside the M05 comparators' training support (all 168-row training-fold rows).
- **Fairness statement (fixed wording, included in the output and the manuscript):** "M14 is a matched held-out evaluation-row comparison under inherited folds, but training support may differ between methods. It therefore does not establish method superiority when effective training populations differ." The M05 methods are **not** refit to equalise training support.

### 3.11 Outputs
`M14_GATE1_RELEASED_METHOD_AUDIT.md`, `M14_GATE2_BRIDGE_RESIDUALS.csv`, `M14_BRIDGE_EXCLUSIONS.csv`, `M14_GATE3_CORRESPONDENCE.csv`, and if Gate 4 runs, `M14_BASELINE_METRICS.csv`, `M14_PAIRED_DELTAS.csv`, `M14_COVERAGE.csv`, plus `M14_DECISION.md` stating which pre-committed outcome occurred.

---

## 4. R4 freeze (after M12–M14)

- One append-only notebook builds R4. It references the R3_2 bundle hash and the M12/M13/M14 bundle hashes, and adds their tables as new manuscript or supplementary items.
- No R3_2 table, figure or ledger row is edited.
- The checks must pass: input hashes match, M12 consistency checks pass, M13 and M14 record their gate and interpretation status.
- After R4: manuscript writing only. Any new idea goes into the future-research log.

---

## 5. Amendments
(None. Any amendment is added here with a date, reason, and the SHA-256 of the pre-amendment file.)
