import unittest
import sys
import os

# Ensure the parent directory is on the path so we can import from dsa.hashmap
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dsa.hashmap.log_analyzer import (
    count_events,
    find_most_common,
    find_least_common,
    render_report,
)
from dsa.hashmap.contributor_frequency import (
    count_commits_by_developer,
    sort_leaderboard,
    render_leaderboard,
)

class TestDSALogAnalyzer(unittest.TestCase):
    def test_count_events(self):
        events = ["COMMIT", "PR_CREATED", "COMMIT", "REVIEW", "COMMIT"]
        expected = {"COMMIT": 3, "PR_CREATED": 1, "REVIEW": 1}
        self.assertEqual(count_events(events), expected)

    def test_find_most_and_least_common(self):
        frequency = {"COMMIT": 5, "PR_CREATED": 2, "REVIEW": 1}
        self.assertEqual(find_most_common(frequency), ("COMMIT", 5))
        self.assertEqual(find_least_common(frequency), ("REVIEW", 1))

    def test_empty_frequency_error(self):
        with self.assertRaises(ValueError):
            find_most_common({})
        with self.assertRaises(ValueError):
            find_least_common({})


class TestDSAContributorLeaderboard(unittest.TestCase):
    def test_count_commits_by_developer(self):
        commits = [
            {"hash": "1", "developer": "Alice"},
            {"hash": "2", "developer": "Bob"},
            {"hash": "3", "developer": "Alice"},
        ]
        expected = {"Alice": 2, "Bob": 1}
        self.assertEqual(count_commits_by_developer(commits), expected)

    def test_sort_leaderboard(self):
        commit_counts = {"Bob": 2, "Alice": 5, "Charlie": 2}
        # Alice (5), then Bob (2) and Charlie (2) sorted alphabetically
        expected = [("Alice", 5), ("Bob", 2), ("Charlie", 2)]
        self.assertEqual(sort_leaderboard(commit_counts), expected)


if __name__ == "__main__":
    unittest.main()
