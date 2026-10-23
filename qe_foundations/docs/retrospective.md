# Retrospective -- Thursday pair exercise (SQL validation)

<!--
HOW TO USE: copy this file to  qe_foundations/docs/retrospective.md  and answer every
"##" section below (keep the headings). Write TOGETHER in the last 15 minutes; both
partners must agree with what is written. Aim for 2-4 specific sentences per section
(about 250-400 words in total). "It went well" is not an answer: name a rule, a
moment, a query, a commit.
Delete nothing except these comments.
-->

## Pair and branch

Aiden Ford and Kevin Nguyen worked together on the shared repository `qe-foundations` on the branch `feature/sql-validation-a-k`. We completed all exercise requirements and wrapped up our work with final commit hash ``.


## What we built

Our repository now contains a complete data quality framework including 14 SQL validation queries (`sql/validation_queries.sql`), a custom `ValidationFailedError` exception, a Python runner with dual-level file/console logging (`qe_foundations/validation/runner.py`), 7 passing unit tests (`qe_foundations/tests/test_validation.py`), and defect documentation. The suite ends with 12 validation rules (R-01 through R-12) and 2 expectation rules (E-01 and E-02). Running `python -m qe_foundations.validation` executes all rules sequentially, prints color-coded PASS, FAIL, and INFO lines for each rule with indented evidence for violations, and outputs a final summary line showing total PASS, FAIL, and INFO counts.


## How the pairing worked

The driver/navigator worked together for each Block and ensured equal contribution to the codebase. One concrete moment of navigator value occurred during Block 3 on rule R-12, where the navigator reminded the driver that SQLite's `LIKE` operator is case-insensitive, catching `b-1048` before we committed the query. A moment where pairing felt awkward was during Block 1 setup when syncing git branches and managing virtual environments across two different local machines. To resolve this, we established a strict "pull before you drive" habit before starting each new 30-minute block.


## The hardest rule

Rule R-12 (`build_id` format and casing) took the longest to implement correctly because SQLite's default string matching ignores casing for standard ASCII letters. Our first wrong query was `SELECT run_id, build_id FROM test_runs WHERE build_id IS NULL OR build_id NOT LIKE 'B-____';` which incorrectly passed lowercase build IDs like `b-1048` and returned 0 violating rows instead of catching them. We fixed this by adding an explicit exact-case check `OR build_id <> UPPER(build_id)`, which properly caught the lowercase and improperly formatted build IDs.


## A surprise in the data

We were surprised to discover test run `5004`, which had a `duration_ms` of `0` and status `SKIPPED`. We initially thought 0 ms was an invalid duration defect, but upon reviewing the rule specification, we realized skipped tests logically take no execution time and are legitimate rows. If we were speaking with the product owner, we would ask whether a duration of `0` ms should ever be permitted for tests with status `PASSED`, or if `0` ms must strictly be restricted to `SKIPPED` tests.


## SQLite and SQL pitfalls we hit

We ran into SQLite's handling of `NULL` values when writing rules with `NOT IN` (like R-03 and R-07) and `NOT BETWEEN` (R-06), where `NULL` rows are silently excluded from evaluation rather than flagged as violations. Additionally, operator precedence between `AND` and `OR` bit us in rule R-11 until we wrapped the conditional logic in explicit parentheses. In the future, we will spot these traps early by explicitly checking for `IS NULL` on optional columns and always grouping compound logical conditions with parentheses.


## Skills we connected from this week

From Monday, we applied virtual environment isolation and feature-branch Git workflows (`git switch`, `git pull`, and branch merging). From Tuesday, we built a custom Python exception subclassing `Exception` (`ValidationFailedError`) to carry rich error metadata (`rule_id`, `description`, and `rows`). From Wednesday, we used `logging.getLogger` with separate console (`INFO`) and file (`DEBUG`) handlers, and wrote isolated `unittest` test cases using `setUp` and `assertRaises`.


## What we would do differently

For our next pair session, we would allocate 5 minutes at the start of each block to outline the exact query logic on paper before typing in the editor. From Friday's upcoming milestone, we need SQL `JOIN` operations and `GROUP BY` aggregations to cross-validate test runs against suite metadata tables and detect multi-row aggregate anomalies like duplicate execution attempts.

