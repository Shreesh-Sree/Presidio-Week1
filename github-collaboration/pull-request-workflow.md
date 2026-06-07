# Pull Request Workflow

Pull requests are where the project starts feeling like team work. At first I thought a PR was just a way to merge code, but it is also where reviewers understand the change.

## PR Notes I Would Write

```markdown
## What changed
- Added developer activity event counting.
- Added most common and least common event reporting.

## How I tested
- Ran `python dsa/hashmap/log_analyzer.py`
- Checked that CI passed Python syntax validation.

## Notes for reviewer
- Uses dictionaries for O(n) frequency counting.
- File input is not added yet.
```

## Three-Developer Simulation

### Developer A: HashMap Analytics

```bash
git checkout -b feature/hashmap
python dsa/hashmap/log_analyzer.py
git add dsa/hashmap
git commit -m "Implement developer activity log analyzer"
git push -u origin feature/hashmap
```

Developer A opens a PR titled `Add HashMap analytics for activity logs`.

### Developer B: Recursion and System Design

```bash
git checkout main
git pull origin main
git checkout -b feature/recursion
git add dsa/recursion
git commit -m "Add recursive repository analyzers"
git push -u origin feature/recursion
```

Later, Developer B starts the architecture work:

```bash
git checkout main
git pull origin main
git checkout -b feature/system-design
git add system-design
git commit -m "Document developer analytics platform architecture"
git push -u origin feature/system-design
```

### Developer C: SQL Analytics

```bash
git checkout main
git pull origin main
git checkout -b feature/sql
git add sql
git commit -m "Add SQL schema and engineering analytics queries"
git push -u origin feature/sql
```

## Review Checklist

When reviewing, I would check:

- Is the change focused?
- Can I understand the names without extra explanation?
- Does the script run?
- Are edge cases mentioned somewhere?
- Is complexity documented?
- Did CI pass?

## Merge Process

```bash
git checkout main
git pull origin main
git merge --squash feature/sql
git commit -m "Add SQL developer productivity analytics"
git push origin main
```

After testing this flow, I noticed that deleting old branches keeps the repo easier to read:

```bash
git branch -d feature/sql
git push origin --delete feature/sql
```

## Lesson Learned

A good pull request is not just "please merge this." It should give the reviewer enough context to trust the change.

