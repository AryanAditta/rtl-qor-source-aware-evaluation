# Quick verification

The released manuscript-facing prediction tables can be checked without rerunning synthesis, STA or model training.

```bash
git clone https://github.com/AryanAditta/rtl-qor-source-aware-evaluation.git
cd rtl-qor-source-aware-evaluation
python -m pip install -r requirements.txt
python analysis/recompute_primary_metrics.py
```

The script reads only the compact files in `data/` and reports:

- Reserve50 prospective Area native vs graph-primary results;
- Source50 prospective Timing native vs TimingV2 results;
- the saved-style 5,000-resample percentile intervals using the frozen seeds (143 and 149);
- Source50 secondary Area metrics;
- the all-83 External83 Area/Timing results;
- the named `pipelineTop` Timing case and the manuscript's post-hoc without-`pipelineTop` sensitivity.

The expected primary values are approximately:

- Reserve50 Area: native MAE 8,381.57 µm², candidate MAE 3,014.99 µm², macro log1p delta −0.311442, 95% interval [−0.504499, −0.142821], 27/39 lower candidate errors.
- Source50 Timing: native MAE 0.166539 ns, candidate MAE 0.136291 ns, macro log1p delta −0.016546, 95% interval [−0.028422, −0.004974], 27/39 lower candidate errors.

These checks operate on frozen prediction-level evidence only. They do not create new experimental evidence or change the R4.1 freeze.
