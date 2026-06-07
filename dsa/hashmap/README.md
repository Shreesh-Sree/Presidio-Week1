# HashMap Analytics

While working on this module, I explored how dictionaries can be used for simple engineering analytics. Initially I almost made this a plain word counter, but that felt too disconnected from the repo theme. I changed it to count developer workflow events instead.

## `log_analyzer.py`

This script counts events like:

- `COMMIT`
- `PR_CREATED`
- `REVIEW`

It prints the frequency count, the most common event, and the least common event.

Run:

```bash
python dsa/hashmap/log_analyzer.py
```

Why a dictionary made sense:

- Event names are the keys.
- Counts are the values.
- Updating a count is simple and fast.

Complexity:

- Time: `O(n)`
- Space: `O(k)`, where `k` is the number of unique event types

## `contributor_frequency.py`

This script counts commits per developer and prints a small leaderboard.

I considered sorting commits first, but that would make the solution more complicated than needed. Counting with a dictionary first and sorting only the final developer totals felt cleaner.

Run:

```bash
python dsa/hashmap/contributor_frequency.py
```

Complexity:

- Counting: `O(n)`
- Sorting leaderboard: `O(d log d)`
- Space: `O(d)`, where `d` is the number of developers

## Lessons Learned

- HashMaps are not just for interview problems. They are very useful for quick metrics.
- The input data matters. Once I used commits and reviews, the exercise felt more realistic.
- A leaderboard needs sorting, so the total complexity is not only the dictionary pass.

## TODO

- Read activity logs from a file.
- Add date-based filtering, like "last 7 days".
- Handle unknown event types more explicitly.

