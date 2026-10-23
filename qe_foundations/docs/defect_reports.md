# Defect reports (top 2 findings)

<!--
HOW TO USE: copy this file to  qe_foundations/docs/defect_reports.md.
Choose the TWO most serious defect groups your suite found (think: money, customers,
automation reliability). Write each as a real bug report using the structure from the
lesson "Using SQL for QA Data Validation", section "Reporting what you find".
Keep the "Title:" labels (the check script counts them) and paste the exact SQL.
-->

## Defect report 1

**Title:** test_run stores negative and missing durations

**Rule:** R-04

**Environment / when:** 
Inside the test_runs table in the database
Reproduced by running python -m qe_foundations.validation --show R-04

**Query:**

```sql
SELECT run_id, duration_ms
FROM test_runs
WHERE duration_ms < 0 OR duration_ms IS NULL;
```

**Evidence:** 
run_id | duration_ms
-------+------------
5009   | -250
5016   | NULL

**Impact:** Average run would be affected by this a lot and it could lead to misleading results, as well as with total run time. 

**Severity (suggested) and why:** High. It corrupts a very important value that everyone will need.

**Question or false-alarm check:** Negative values could possibly be ok if the rule was defined to allow negative durations for skipped tests.

## Defect report 2

**Title:** Mismatched failure messages relative to test execution status

**Rule:** R-11 | Consistency | FAILED/ERROR runs need a failure_message; PASSED runs must not have one

**Environment / when:** SQLite in-memory database, test_runs_seed.sql

**Query:**

```sql
SELECT run_id, status, failure_message
FROM test_runs
WHERE (status IN ('FAILED', 'ERROR') AND (failure_message IS NULL OR TRIM(failure_message) = ''))
   OR (status = 'PASSED' AND failure_message IS NOT NULL AND TRIM(failure_message) <> '');
```

**Evidence:** 
Run 5003: FAILED status with a NULL message (missing failure reason).
Run 5012: PASSED status with an unexpected warning string.
Run 5033: ERROR status with a blank string ('') message.

**Impact:** Delays automated debugging since failed runs lack error context, while passed runs containing warnings can trigger false alarms in monitoring dashboards.

**Severity (suggested) and why:** Medium — Impedes automated test telemetry and troubleshooting reliability.

**Question or false-alarm check:** Confirmed via schema rules that the failure_message column is intended strictly for failure or error contexts.
