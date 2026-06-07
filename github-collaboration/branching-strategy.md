# Branching Strategy

For this project I used a simple feature-branch strategy. I wanted the repo to show how work would be split between developers instead of making every change directly on `main`.

## Branches I Planned

| Branch | What it contains | Simulated owner |
| --- | --- | --- |
| `main` | Reviewed version of the repo | Team |
| `feature/hashmap` | Activity counting and contributor leaderboard | Developer A |
| `feature/recursion` | Folder and dependency traversal | Developer B |
| `feature/sql` | Schema, sample data, joins, indexes, transactions | Developer C |
| `feature/system-design` | Architecture notes and diagrams | Developer B |
| `feature/sdlc` | SDLC notes and learning journal | Developer A |

I know this is a small project, so all these branches may feel like extra process. I still included them because the point is to practice collaboration habits early.

## Basic Flow

```bash
git checkout main
git pull origin main
git checkout -b feature/hashmap

# make focused changes
git add dsa/hashmap README.md
git commit -m "Add hashmap based developer activity analytics"
git push -u origin feature/hashmap
```

After this, the developer opens a pull request into `main`.

## What I Would Put in a PR

- What changed
- Why I made the change
- How I tested it
- Anything I am unsure about

Example:

```text
Added log_analyzer.py for counting developer activity events.
Tested with the sample event list.
Still need to add file input later.
```

## Commit Style

I tried to keep commit messages specific:

```bash
git commit -m "Add PR event frequency analyzer"
git commit -m "Document hashmap complexity analysis"
git commit -m "Add CI syntax validation"
```

One issue I faced when learning Git was writing messages like `update` or `final`. They are quick, but they are not helpful when reviewing history later.

## Merge Strategy

For a small internship repo, squash merge is reasonable because it keeps `main` clean:

```bash
git checkout main
git pull origin main
git merge --squash feature/hashmap
git commit -m "Add hashmap analytics module"
git push origin main
```

## TODO

- Add real screenshots after the repo is pushed to GitHub.
- Try one actual merge conflict and document the exact resolution.
- Add a pull request template file later.

