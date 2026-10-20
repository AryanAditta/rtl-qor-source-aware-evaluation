# M13 development-only interpretation

Proper538: 538 rows / 398 source components, inherited five folds. Primary seed: 42; extra full-model seeds: [1, 2, 3, 4, 5].
Reproducibility status: **ENVIRONMENT_DIFFERENT**. Use M13_REPRODUCIBILITY_CHECKS.csv for exact historical gaps.
Observed full-model seed envelope N_seed = 0.0010327670016971602. 5/8 leave-family-out effects are within this observed seed noise.

**A small effect does not imply a family is unimportant, because correlated families can substitute for one another.**
F5 and F6 are small and receive no individual claims. The intervals are descriptive and unadjusted; there are no p-values or significance claims.

- F1 (Operator widths): removed-minus-full macro log error 0.015319448093896461; descriptive 95% interval [0.0051127770504945562, 0.026784132992264842]; larger in magnitude than the observed five-extra-seed envelope.
- F2 (Chain and width interaction): removed-minus-full macro log error -0.00092394174914237222; descriptive 95% interval [-0.0039337654181819514, 0.0020640072413258123]; within seed noise.
- F3 (Depth and topology): removed-minus-full macro log error -0.00092030317012879498; descriptive 95% interval [-0.002616204180911067, 0.00087134323478845963]; within seed noise.
- F4 (Structural density): removed-minus-full macro log error 0.0010529385199731284; descriptive 95% interval [-0.00094914005554389447, 0.0030614940944118005]; larger in magnitude than the observed five-extra-seed envelope.
- F5 (Memory structure): removed-minus-full macro log error 0.00096755559413440871; descriptive 95% interval [-0.0012050402389670843, 0.0032133921302633932]; within seed noise.
- F6 (Endpoint and interface): removed-minus-full macro log error -0.00066540012711464294; descriptive 95% interval [-0.0026752309511217059, 0.0014186293098111323]; within seed noise.
- F7 (Clock control and design type): removed-minus-full macro log error 0.0012902780853325444; descriptive 95% interval [-0.0017696015931865665, 0.0044766676933414608]; larger in magnitude than the observed five-extra-seed envelope.
- F8 (Connectivity diagnostics): removed-minus-full macro log error -0.00099091385786214542; descriptive 95% interval [-0.0027604751758006103, 0.00074243607067374026]; within seed noise.

A removal that lowers observed development error remains a descriptive finding. It does not license a new candidate, feature selection or TimingV3. No fresh status changes. No full-data deployment fit or calibration was performed.

**Required manuscript placement:** at least one sentence in main Timing Results, irrespective of direction. The full table/figure may be supplementary.

Suggested factual sentence: On Proper538, the eight predefined TimingV2 family-removal contrasts were evaluated under inherited source-component folds; 5/8 were within the observed full-model seed envelope. This descriptive ablation did not change the frozen TimingV2 candidate.

Numerical-library versions differ from Stage146. All family contrasts use this M13 run’s own primary-seed full-model rerun; the historical discrepancy is reported separately and is not attributed to a family.
