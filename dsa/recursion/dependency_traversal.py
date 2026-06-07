"""Traverse repository module dependencies recursively.

Sample execution:
    $ python dsa/recursion/dependency_traversal.py
    Traversal order from api:
      api
      analytics
      database
      cache
      auth

Complexity:
    Time: O(v + e), where v is modules and e is dependency edges.
    Space: O(v), for visited modules and recursion stack.
"""

from __future__ import annotations


DependencyGraph = dict[str, list[str]]


SAMPLE_DEPENDENCIES: DependencyGraph = {
    "api": ["analytics", "auth"],
    "analytics": ["database", "cache"],
    "auth": ["database"],
    "database": [],
    "cache": [],
}

# TODO: Add explicit cycle reporting instead of only skipping visited modules.


def traverse_dependencies(
    graph: DependencyGraph,
    module: str,
    visited: set[str] | None = None,
) -> list[str]:
    """Return a depth-first recursive dependency traversal order."""
    if visited is None:
        visited = set()

    if module in visited:
        # Current Week-1 behavior: skip duplicates to avoid repeated work.
        return []

    visited.add(module)
    order = [module]

    for dependency in graph.get(module, []):
        order.extend(traverse_dependencies(graph, dependency, visited))

    return order


def describe_recursion_tree(graph: DependencyGraph, module: str, depth: int = 0) -> str:
    """Render the recursive dependency tree as indented text."""
    lines = [f"{'  ' * depth}{module}"]
    for dependency in graph.get(module, []):
        lines.append(describe_recursion_tree(graph, dependency, depth + 1))
    return "\n".join(lines)


def main() -> None:
    """Run the sample dependency traversal."""
    traversal = traverse_dependencies(SAMPLE_DEPENDENCIES, "api")
    print("Traversal order from api:")
    for module in traversal:
        print(f"  {module}")
    print("\nRecursion tree:")
    print(describe_recursion_tree(SAMPLE_DEPENDENCIES, "api"))


if __name__ == "__main__":
    main()
