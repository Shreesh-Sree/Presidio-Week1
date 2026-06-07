# SDLC for DevInsight-Lab

I used DevInsight-Lab itself as the SDLC example. This helped because I could connect each SDLC phase to something I actually did in the repo.

## 1. Requirements

The requirements were clear at a high level: include GitHub collaboration, HashMaps, recursion, SQL joins, indexing, transactions, SDLC, system design, and CI.

The part I had to decide was the theme. I chose developer productivity analytics because it connects naturally to commits, PRs, reviews, and repositories.

## 2. Design

I split the repo by learning area:

- `github-collaboration/` for team workflow notes
- `dsa/` for HashMap and recursion scripts
- `sql/` for relational analytics
- `system-design/` for architecture notes
- `learning-journal/` for reflection
- `.github/workflows/` for CI

One design choice I made was to keep the Python scripts small and runnable. I could have built one larger app, but for Week-1 it was easier to review smaller modules.

## 3. Development

The intended workflow is feature branches:

```bash
git checkout -b feature/sql
git add sql
git commit -m "Add SQL analytics schema and queries"
git push -u origin feature/sql
```

Initially I built a lot locally, but if I repeat this project I would create and merge each branch more gradually.

## 4. Testing

Testing for this Week-1 version includes:

- running the Python scripts locally
- compiling Python files with `py_compile`
- checking that required folders exist in CI
- reading SQL queries for schema consistency
- reviewing markdown for clarity

This is not full production testing yet. It is a starter safety net.

## 5. Deployment

For this project, deployment means publishing the repository to GitHub with GitHub Actions enabled. There is no running web app yet.

## 6. Maintenance

Future maintenance work:

- add unit tests
- add a PostgreSQL setup guide
- add a small API service
- add dashboard mockups
- improve SQL performance notes

## Lessons Learned

The SDLC is easier to understand when applied to something small. Even a learning repo benefits from requirements, design decisions, testing, and future maintenance notes.

