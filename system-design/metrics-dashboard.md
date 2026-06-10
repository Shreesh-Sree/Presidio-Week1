# Metrics Dashboard - Repository Health & Review Metrics

This document describes the layout specifications for the developer activity dashboard.

## 1. Overview Dashboard Layout
The dashboard UI displays high-level activity metrics in real-time.

```text
+-------------------------------------------------------------------------+
| [LOGO] DevInsight-Lab Analytics                   (User: Admin) [Logout]|
+-------------------------------------------------------------------------+
|  [Summary Cards]                                                        |
|  +------------------+  +------------------+  +------------------+       |
|  | Active Repos: 4  |  | Total Commits: 89|  | Merged PRs: 14   |       |
|  +------------------+  +------------------+  +------------------+       |
+-------------------------------------------------------------------------+
|  [Charts]                                                               |
|  +---------------------------------+  +-------------------------------+ |
|  | PR Cycle Time (Days)            |  | Commits Leaderboard           | |
|  | 5d |**                          |  | 1. Anika Rao (24)             | |
|  | 4d |****                        |  | 2. Mateo Chen (18)            | |
|  | 3d |*******                     |  | 3. Priya Shah (12)            | |
|  +---------------------------------+  +-------------------------------+ |
+-------------------------------------------------------------------------+
```

---

## 2. Key Metrics Tracked
- **PR Cycle Time**: The average hours/days between PR creation and merge. Helpful for measuring process efficiency.
- **Review Latency**: Average hours review feedback takes to complete.
- **Commit Volume**: Total commits parsed per repository.
- **Merge/Reject Ratio**: Visual comparison of merged vs rejected/closed PRs.
