"""Unit tests for the validation runner (Wednesday: unittest).

Run from the repository root:
    python -m unittest qe_foundations.tests.test_validation -v

Two tests are provided and already pass. The others are TODO stubs that FAIL on
purpose (self.fail) until you replace them. You need at least 5 passing tests in
total, including one that uses assertRaises with ValidationFailedError and one
that proves a rule really catches a known planted defect.

Remember (Wednesday): arrange / act / assert, one idea per test, a descriptive
test name, and each test builds its own fresh in-memory database in setUp.
"""
import unittest

from qe_foundations.validation import runner
from qe_foundations.validation.exceptions import ValidationFailedError


class ValidationRunnerTests(unittest.TestCase):
    def setUp(self):
        self.conn = runner.connect(":memory:")
        runner.load_seed(self.conn)
        self.addCleanup(self.conn.close)

    # ---- provided -----------------------------------------------------------
    def test_seed_loads_expected_number_of_rows(self):
        (count,) = self.conn.execute("SELECT COUNT(*) FROM test_runs").fetchone()
        self.assertEqual(count, 60)

    def test_parse_rules_finds_the_required_rule_ids(self):
        ids = {rule.rule_id for rule in runner.parse_rules()}
        required = {f"R-{n:02d}" for n in range(1, 13)} | {"E-01", "E-02"}
        self.assertTrue(required <= ids, f"missing rules: {sorted(required - ids)}")

    # ---- TODO: replace each self.fail with a real test ----------------------
    def test_run_rule_returns_rows_when_rule_holds(self):
        # Arrange: a Rule whose SQL returns no rows (e.g. WHERE run_id = -1) and expect=0
        rule = runner.Rule(
            rule_id="T-01",
            dimension="Test",
            description="no run has id -1",
            sql="SELECT run_id FROM test_runs WHERE run_id = -1;",
            expect=0,
        )
        # Act:     runner.run_rule(self.conn, rule)
        rows = runner.run_rule(self.conn, rule)
        # Assert:  the result is an empty list and no exception was raised
        self.assertEqual(rows, [])

    def test_run_rule_raises_validation_failed_error_with_the_evidence(self):
        # Arrange: a Rule whose SQL returns run 5003 (WHERE run_id = 5003), expect=0
        rule = runner.Rule(
            rule_id="T-02",
            dimension="Test",
            description="returns run 5003",
            sql="SELECT run_id FROM test_runs WHERE run_id = 5003;",
            expect=0
        )
        # Act/Assert: with self.assertRaises(ValidationFailedError) as ctx: ...
        with self.assertRaises(ValidationFailedError) as ctx:
            runner.run_rule(self.conn, rule)
        #             then assert ctx.exception.rule_id and ctx.exception.rows
        self.assertEqual(ctx.exception.rule_id, "T-02")
        self.assertEqual(ctx.exception.rows, [(5003,)])

    def test_duration_rule_catches_the_known_bad_runs(self):
        # Arrange: find rule R-04 in runner.parse_rules()
        rules = runner.parse_rules()
        rule = next(r for r in rules if r.rule_id == "R-04")
        # Act:     rows = runner.fetch_rows(self.conn, rule.sql)[1]
        rows = runner.fetch_rows(self.conn, rule.sql)[1]
        run_ids = {row[0] for row in rows}
        # Assert:  the run_ids you PREDICTED (from your own defect checklist) are returned
        self.assertIn(5009, run_ids)
        self.assertIn(5016, run_ids)

    def test_expectation_rule_fails_when_the_expected_row_is_missing(self):
        # Arrange: a Rule with expect=1 whose SQL matches NOTHING (WHERE run_id = -1)
        rule = runner.Rule(
            rule_id="T-04",
            dimension="Test",
            description="returns nothing",
            sql="SELECT run_id FROM test_runs WHERE run_id = -1;",
            expect=1
        )
        # Assert:  run_rule raises ValidationFailedError
        with self.assertRaises(ValidationFailedError):
            runner.run_rule(self.conn, rule)
        


if __name__ == "__main__":
    unittest.main()
