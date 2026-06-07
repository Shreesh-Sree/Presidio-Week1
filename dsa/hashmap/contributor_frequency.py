"""Build a contributor leaderboard from commit ownership data.

Sample execution:
    $ python dsa/hashmap/contributor_frequency.py
    Contributor leaderboard:
      1. Anika Rao - 4 commits
      2. Mateo Chen - 3 commits
      3. Priya Shah - 2 commits

Complexity:
    Time: O(n + d log d), where n is commits and d is developers.
    Space: O(d), where d is the number of unique contributors.
"""

from __future__ import annotations


DEFAULT_COMMITS: list[dict[str, str]] = [
    {"hash": "a1c9f2", "developer": "Anika Rao"},
    {"hash": "b42e10", "developer": "Mateo Chen"},
    {"hash": "f8d331", "developer": "Anika Rao"},
    {"hash": "c02a77", "developer": "Priya Shah"},
    {"hash": "d903ac", "developer": "Mateo Chen"},
    {"hash": "e72bd0", "developer": "Anika Rao"},
    {"hash": "ab3491", "developer": "Anika Rao"},
    {"hash": "ff92bc", "developer": "Priya Shah"},
    {"hash": "19bd01", "developer": "Mateo Chen"},
]

# TODO: Replace in-memory sample commits with parsed Git log data later.


def count_commits_by_developer(commits: list[dict[str, str]]) -> dict[str, int]:
    """Count commits per developer using a dictionary."""
    leaderboard: dict[str, int] = {}
    for commit in commits:
        developer = commit["developer"]
        leaderboard[developer] = leaderboard.get(developer, 0) + 1
    return leaderboard


def sort_leaderboard(commit_counts: dict[str, int]) -> list[tuple[str, int]]:
    """Sort contributors by commit count descending, then name ascending."""
    # Sorting by name as a tie-breaker keeps the output stable for review.
    return sorted(commit_counts.items(), key=lambda item: (-item[1], item[0]))


def render_leaderboard(commits: list[dict[str, str]]) -> str:
    """Return a formatted contributor leaderboard."""
    commit_counts = count_commits_by_developer(commits)
    sorted_counts = sort_leaderboard(commit_counts)

    lines = ["Contributor leaderboard:"]
    for rank, (developer, count) in enumerate(sorted_counts, start=1):
        lines.append(f"  {rank}. {developer} - {count} commits")
    return "\n".join(lines)


def main() -> None:
    """Run the sample contributor frequency analysis."""
    print(render_leaderboard(DEFAULT_COMMITS))


if __name__ == "__main__":
    main()
