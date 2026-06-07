# Recursion Analytics

This module helped me practice recursion using repository-shaped data. Recursion made more sense once I stopped thinking of it as a trick and started drawing the folder tree.

## `folder_analyzer.py`

This script recursively walks a nested repository model and reports:

- total files
- total folders
- maximum depth

Run:

```bash
python dsa/recursion/folder_analyzer.py
```

One issue I faced was deciding what the base case should return. I used a list of files as the base case because that is where the recursive nesting stops.

Complexity:

- Time: `O(n)` for all files and folders
- Space: `O(h)` for recursion depth

## `dependency_traversal.py`

This script performs a depth-first traversal over a small dependency graph.

```text
api
  analytics
    database
    cache
  auth
    database
```

I noticed that dependencies can repeat. For example, both `analytics` and `auth` can depend on `database`. I added a `visited` set so the traversal does not process the same module again.

Complexity:

- Time: `O(v + e)`
- Space: `O(v)`

## Lessons Learned

- Recursion needs a clear stopping point.
- A recursion tree is easier to understand than only reading code.
- Graph recursion usually needs a `visited` set.

## TODO

- Add cycle detection messages instead of silently skipping visited nodes.
- Try the same traversal iteratively with a stack and compare both versions.
- Support reading dependency data from JSON.

