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
| R-05 | | | |
| R-06 | | | |
| R-07 | | | |
| R-08 | | | |
| R-09 | | | |
| R-10 | | | |
| R-11 | | | |
| R-12 | | | |

## Decoys: rows that look odd but are LEGAL (we must not flag them)

<!-- List at least two run_ids and say why they are fine, e.g. "run 5xxx: SKIPPED with 0 ms -- skipped tests take no time." -->


## Rows reported by more than one rule

<!-- Which run_ids appear in two or more rules? Is that OK? (Each rule must be testable on its own.) -->


## Open questions for the product owner

<!-- Rules that are really business decisions (like "is a price of 0 allowed?" in the lesson). -->

