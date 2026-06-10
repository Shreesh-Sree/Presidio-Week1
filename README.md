# DevInsight-Lab

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-informational)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![Status](https://img.shields.io/badge/Internship-Week%201-brightgreen)

DevInsight-Lab is my Week-1 SDE internship repository. I wanted to avoid building another generic practice repo, so I chose a theme that feels closer to real engineering work: developer activity, commits, pull requests, reviews, repositories, and productivity analytics.

This is not a finished product. It is more like a small lab where I connected GitHub workflow, DSA basics, SQL, transactions, indexing, SDLC, CI, and system design into one project.

## Why I Built This

Initially I was treating each topic separately: Git in one place, HashMaps somewhere else, SQL as a different exercise. That made the repo feel disconnected. I decided to use developer productivity analytics as the common thread because most SDE work already happens around commits, PRs, reviews, and CI checks.

The goal was to make Week-1 concepts feel practical instead of only academic.

## Repository Structure

```text
DevInsight-Lab/
|-- .github/workflows/ci.yml
|-- docs/internship-summary.md
|-- dsa/
|   |-- hashmap/
|   `-- recursion/
|-- github-collaboration/
|-- learning-journal/week1.md
|-- sdlc/project-sdlc.md
|-- sql/
`-- system-design/
```

## What Is Inside

### GitHub Collaboration

I documented a simple feature-branch workflow using branches like:

- `feature/hashmap`
- `feature/recursion`
- `feature/sql`
- `feature/system-design`
- `feature/sdlc`

The collaboration docs include pull request steps, review expectations, merge flow, and a small merge conflict simulation. One thing I noticed is that Git commands are easy to memorize, but the harder part is understanding why teams avoid pushing directly to `main`.

### DSA Modules

The DSA part uses the same developer workflow theme:

- `log_analyzer.py` counts commit, PR, and review events using dictionaries.
- `contributor_frequency.py` builds a commit leaderboard.
- `folder_analyzer.py` recursively analyzes a repository-like folder tree.
- `dependency_traversal.py` recursively walks module dependencies.

Run them:

```bash
python dsa/hashmap/log_analyzer.py
python dsa/hashmap/contributor_frequency.py
python dsa/recursion/folder_analyzer.py
python dsa/recursion/dependency_traversal.py
```

After testing the scripts, I realized the interesting part was not just getting the output. It was choosing data that actually sounds like something an engineering team might track.

### SQL

The SQL folder models:

- developers
- repositories
- commits
- pull requests
- reviews

I included joins, grouping, HAVING, subqueries, indexing notes, and a transaction workflow for PR approval. I considered putting review fields directly inside `pull_requests`, but I decided to keep reviews in a separate table. It adds an extra join, but it is cleaner because one PR can have multiple reviews.

### System Design

The system design started simple with users, APIs, a database, and cache. After analyzing the provided `qz.pdf`, I expanded it with ideas like:

- webhook ingestion
- async event processing
- RBAC
- audit logs
- observability
- queue-based workers
- high availability notes

I did not copy the PDF domain. I adapted the architecture patterns to DevInsight-Lab's domain.

### CI/CD

GitHub Actions runs on `push` and `pull_request`. Right now it validates the repository structure and checks Python syntax. It is basic, but it is enough for Week-1 and gives the repo a real review workflow.

## What I Learned

- HashMaps are useful for quick analytics like frequency counts and leaderboards.
- Recursion becomes easier when I draw the tree or trace the call stack.
- SQL joins are easier to understand when the tables represent real product entities.
- Indexes improve read performance, but they also add write overhead.
- Transactions make more sense when tied to workflows like PR approval.
- System design is mostly about tradeoffs, not drawing the biggest diagram possible.

## Challenges I Faced

One issue I faced was making the repository feel connected. At first, the DSA and SQL parts felt like separate assignments. After tying them to engineering workflow data, the project felt more realistic.

Another challenge was system design scope. It is tempting to add every production component, but I tried to keep the design understandable for Week-1 while still showing that I studied a more advanced reference architecture.

## Future Improvements

- [x] Add unit tests for each Python module (implemented in [dsa_test.py](dsa/dsa_test.py)).
- [x] Add a small SQLite or PostgreSQL demo script (implemented in [db_demo.py](sql/db_demo.py)).
- Add SQL linting in CI.
- Create a simple API endpoint for analytics.
- [x] Add dashboard mockups for repository health and review metrics (documented in [metrics-dashboard.md](system-design/metrics-dashboard.md)).
- Track CI checks as another table in the SQL schema.
- Add real GitHub screenshots after practicing the PR workflow.

## Key Takeaways

This repo helped me connect fundamentals with actual engineering workflows. It is still a Week-1 project, but I tried to build it like something I would be comfortable showing to a mentor and improving over time.
