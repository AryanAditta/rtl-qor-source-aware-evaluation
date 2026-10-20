# Frozen manuscript evidence

The files in this directory are compact outputs from the final closure analyses. They are provided as evidence, not as instructions to continue model development.

## M12

`results/m12/` contains the field-comparable metric inventory from already-frozen predictions, the External83 measured-target regime analysis and the metric policy. M12 performed no model fitting, inference or resampling.

## M13

`results/m13/` contains the development-only TimingV2 family ablation, paired family-removal deltas, the observed multi-seed noise envelope and the frozen interpretation. It does not change the selected TimingV2 candidate. The clearest observed family effect is the operator-width family; five of eight removals lie within the observed seed envelope.

## M14

`results/m14/` records the assessed MasterRTL Timing adaptation boundary. Gate 2 retained 167/168 rows in 165/166 components, but Gate 3 had 0/167 designs meeting the frozen 95% usable path-record correspondence rule. Gate 4 therefore did not run, no path model was fitted and no MasterRTL Timing accuracy comparison is reported.

The M14 result is a representation/path-correspondence fidelity boundary of the fixed adapter and evidence chain. It must not be interpreted as a finding that the published MasterRTL Timing method is inaccurate or that TimingV2 outperforms it.

The authoritative manuscript evidence closure is R4.1 under `admin/`.
