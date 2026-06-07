# Merge Conflict Simulation

I included this because merge conflicts were one of the Git topics that felt confusing at first. A conflict is not Git "failing." It usually just means two branches edited the same part of a file and Git needs a human decision.

## Scenario

Developer A updates the README to mention HashMap analytics. Developer C updates the same section to mention SQL dashboards. Both branches are valid, but Git cannot automatically decide which final text should win.

## Reproduce the Conflict

```bash
git checkout main
git checkout -b feature/readme-hashmap
# edit README.md SQL/DSA section
git add README.md
git commit -m "Update README with hashmap analytics summary"

git checkout main
git checkout -b feature/readme-sql
# edit the same README.md lines
git add README.md
git commit -m "Update README with SQL analytics summary"

git checkout feature/readme-sql
git merge feature/readme-hashmap
```

Git marks the conflicting file:

```text
<<<<<<< HEAD
SQL analytics focuses on joins and pull request review metrics.
=======
DSA analytics focuses on HashMap event counting and contributor frequency.
>>>>>>> feature/readme-hashmap
```

## Resolution

Open the file and combine the intent of both changes:

```text
DevInsight-Lab combines DSA analytics, such as HashMap event counting, with SQL analytics for pull request review metrics.
```

Then finish the merge:

```bash
git add README.md
git commit -m "Resolve README analytics summary conflict"
git status
```

## Lesson Learned

After testing a small conflict, I noticed the important part is not just deleting the conflict markers. The real job is preserving the intent from both branches and then running checks again.

## TODO

- Add screenshots from a real GitHub pull request conflict.
- Try resolving a conflict using VS Code's merge editor.
