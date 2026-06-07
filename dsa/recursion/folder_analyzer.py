"""Recursively analyze a repository-like folder tree.

Sample execution:
    $ python dsa/recursion/folder_analyzer.py
    Total files: 7
    Total folders: 6
    Maximum depth: 3

Complexity:
    Time: O(n), where n is the number of nodes in the folder tree.
    Space: O(h), where h is the maximum recursion depth.
"""

from __future__ import annotations

from dataclasses import dataclass


FolderTree = dict[str, "FolderTree | list[str]"]


@dataclass(frozen=True)
class FolderStats:
    """Aggregated folder analytics."""

    total_files: int
    total_folders: int
    max_depth: int


SAMPLE_REPOSITORY: FolderTree = {
    "DevInsight-Lab": {
        "dsa": {
            "hashmap": ["log_analyzer.py", "contributor_frequency.py"],
            "recursion": ["folder_analyzer.py", "dependency_traversal.py"],
        },
        "sql": ["schema.sql", "joins.sql"],
        "docs": ["internship-summary.md"],
    }
}

# TODO: Add support for scanning an actual local directory path.


def analyze_folder(node: FolderTree | list[str], depth: int = 0) -> FolderStats:
    """Recursively calculate files, folders, and maximum depth."""
    if isinstance(node, list):
        # Base case: a file list has no more nested folders to inspect.
        return FolderStats(total_files=len(node), total_folders=0, max_depth=depth)

    total_files = 0
    total_folders = len(node)
    max_depth = depth

    for child in node.values():
        child_stats = analyze_folder(child, depth + 1)
        total_files += child_stats.total_files
        total_folders += child_stats.total_folders
        max_depth = max(max_depth, child_stats.max_depth)

    return FolderStats(total_files, total_folders, max_depth)


def main() -> None:
    """Run the sample recursive folder analysis."""
    stats = analyze_folder(SAMPLE_REPOSITORY)
    print(f"Total files: {stats.total_files}")
    print(f"Total folders: {stats.total_folders}")
    print(f"Maximum depth: {stats.max_depth}")


if __name__ == "__main__":
    main()
