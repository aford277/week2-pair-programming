# Pairing log -- roles and swap schedule

<!--
HOW TO USE: copy this file to  qe_foundations/docs/pairing_log.md.
Fill ONE row at the END of every 30-minute block (it takes one minute). The check
script counts the rows that are filled in; a 3-hour session has 5 driving blocks.
-->

## Roles card (keep it visible)

| | DRIVER | NAVIGATOR |
|---|---|---|
| Hands | the ONLY one on the keyboard | off the keyboard |
| Job | turn the navigator's direction into code; think aloud while typing | read the rule, decide the next step, predict the result, spot typos and edge cases |
| Says things like | "I'm writing the WHERE clause now..." | "Predict first: which run_ids do we expect?" |
| Never | silently type something nobody asked for | grab the mouse or dictate character by character |

**Swap** every 30 minutes, even in the middle of a rule. The outgoing driver commits and pushes
(your own Git name), the new driver runs `git pull`, then types.

## Pair

| | Name | Git user.name (as shown by `git log`) | Machine / repo owner |
|---|---|---|---|
| Partner A | Aiden | aford277 | Aiden |
| Partner B | Kevin | KevinKhangNguyen| Aiden |

Branch: `feature/sql-validation-...`        Remote: `https://github.com/aford277/week2-pair-programming`

## Swap log (one row per block)

| Block | Clock time | Driver | Navigator | Goal of the block | Result (rules done, commit hash) | Predictions: right / wrong |
|---|---|---|---|---|---|---|
| 1 | 1:00 | Aiden | Kevin | Finish R-01 to R-04 | Finished them all, 5f17f57 | Mostly right |
| 2 | 1:30 | Kevin | Aiden | Finish R-05 to R-08 | Got it done, cc2da16 | Mostly right|
| 3 | 2:30 | Aiden | Kevin | Finish rest of rules| R-09 to E-02, 5234b0f | Right|
| 4 | 3:30 | Kevin | Aiden | runner.py file done | Finished, a1edb6a | N/A |
| 5 | 1:30 next day | Aiden | Kevin | Finish test cases | Finished, a010889 | N/A |

## Disagreements and how we settled them

We didn't agree on which defects were the most severe and should be written in the report. We decided we would each do one so that we could both get what we needed.


## Hints we used

We used the level 3 hints to get the skeleton from the hardest rules

