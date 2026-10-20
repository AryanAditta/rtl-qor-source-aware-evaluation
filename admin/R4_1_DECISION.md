# R4.1 evidence closure (append-only addendum to R4)

```json
{
  "run_id": "R4_1_20261017T121855_838848Z",
  "protocol_sha256": "168023aaa7a31a2d5d6f8014245a19e7feed4e17ad2dc1c39225148e34464506",
  "parent_hashes": {
    "R4": "298b1cd1fa2dffe283ad7736dec0d18654facc52136d1ce65d66fa254f5fe00f",
    "M14_3": "5f1098335d86870e123c0e8e85d1763211372f86d6c35e9850526acb788ddb02"
  },
  "R4_status_preserved": "PASS",
  "M12": "COMPLETED_DESCRIPTIVE_FROZEN_METRICS",
  "M13": "COMPLETED_DEVELOPMENT_ABLATION_CANDIDATE_UNCHANGED",
  "M14": "COMPLETED_FEASIBILITY_ATTEMPT_GATE3_ASSESSED_ZERO_CORRESPONDENCE_NO_ACCURACY_COMPARISON",
  "M14_governing_run": "M14_3_20261017T022458_899335Z",
  "M14_superseded_R4_wording": "R4_M14_FEASIBILITY (inputs unavailable; correspondence unassessed)",
  "M14_graphs_hash_identical": 152,
  "M14_gate3_valid_rows": 0,
  "M14_baseline_objective_achieved": false,
  "all_research_objectives_achieved": false,
  "read_only_name_check_confirmed_renaming": true,
  "new_STA_runs": 0,
  "new_model_fits": 0,
  "new_inference": 0,
  "new_resampling": 0,
  "new_target_label_changes": 0,
  "old_records_modified": 0,
  "new_fresh_evidence": false,
  "research_execution_closed": true,
  "next_step": "MANUSCRIPT_WRITING_ONLY;NO_M15;FUTURE_IDEAS_LOGGED"
}
```

M14_3 is the governing M14 record. It reused the corrected M14 Gate 2 receipts, recovered the historical graphs by hash identity, assessed Gate 3 correspondence on all 167 bridge-valid designs and found 0 meeting the frozen 95% rule. No adapted timing-path model was fitted and no baseline accuracy was produced. R4 stays byte-identical and remains the record of M12, M13 and the earlier M14 status; R4.1 supersedes only its M14 wording.

R4.1 adds no experiment, no fit, no inference, no resampling and no label change. Its derived tables count files inside the two hash-verified parent archives. The optional name check only reads hash-verified mapped netlists already on Drive.

After this audit passes, stop experiments and write the manuscript.
