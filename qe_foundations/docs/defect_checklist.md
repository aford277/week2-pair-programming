# Expected-defect checklist (fill in as you go)

<!--
PURPOSE: this is your "answer sheet" for the data. Writing the PREDICTION before you run a
query is the single best habit for catching false passes.
HOW: for each rule, (1) write what you EXPECT in the "Predicted" column BEFORE running the
query, (2) run it, (3) write the run_ids it actually returned in "Defects found (run_ids)"
(comma-separated, 4-digit ids), (4) note anything surprising. Do not delete rows.
check_exercise.py compares this table with what your queries return.
-->

| Rule | Defects found (run_ids) | Predicted (before running) | Notes / surprises |
|---|---|---|---|
| R-01 | 5006, 5019, 5025 | 5006, 5019, 5025 | |
| R-02 | 5011, 5022 | 5011, 5022 | |
| R-03 | 5008, 5014, 5027, 5029 | 5008, 5027, 5029 | 5014 must have extra spaces, we didn't expect it|
| R-04 | 5009, 5016 | 5009, 5016 | |
| R-05 | 5023, 5030 | 5023, 5030 | |
| R-06 | 5013, 5020 | 5013, 5020 | |
| R-07 | 5017, 5024, 5026 | 5017, 5024, 5026 | |
| R-08 | 5014, 5018, 5028 | 5018 | Couldn't see the other trailing spaces |
| R-09 | 5010, 5015, 5035 | 5010, 5015, 5035  | |
| R-10 | 5005, 5032 | 5005, 5032 | |
| R-11 | 5003, 5012, 5033 | 5003, 5012, 5033 | |
| R-12 | 5031, 5034, 5036, 5037 | 5031, 5034, 5036, 5037 | |

## Decoys: rows that look odd but are LEGAL (we must not flag them)

5042 looks odd since the duration is 0. But it's on a skipped run so it's ok.
5041 looks bad since it is exactly 600000 ms but that's the exact stopping point so it is ok


## Rows reported by more than one rule

5014 does. That could be bad since rules should be all on their own.
The reason is R-03 checks the status to find an exact match and R-08 also checks if there is any trailing spaces.


## Open questions for the product owner

Is R-02 strict enough? 
