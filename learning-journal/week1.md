# Week 1 Learning Journal

## Day 1 - Git and Repository Setup

### What I learned

Today I focused on setting up the repository structure and thinking through branch names. I learned that a good folder structure makes the rest of the project less confusing.

### What confused me initially

Initially I tried thinking of each topic as a separate mini assignment. That made the repo feel scattered.

### How I figured it out

I picked one theme, developer productivity analytics, and then mapped every topic to that theme. Git became collaboration, HashMaps became activity counting, and SQL became repository analytics.

### What I would improve next

I would initialize the GitHub repo earlier and push each feature branch separately instead of building most of it locally first.

## Day 2 - GitHub Collaboration

### What I learned

I learned how feature branches and pull requests help teams avoid messy direct changes to `main`.

### What confused me initially

Merge conflicts looked scary at first because Git shows conflict markers inside the file. I was not sure whether Git was broken or just asking me to choose.

### How I figured it out

I created a small conflict simulation and resolved it manually. After that, I understood that a conflict is just Git saying, "both branches changed this part."

### What I would improve next

I want to add actual screenshots from GitHub after pushing the repository.

## Day 3 - HashMap Analytics

### What I learned

Today I used Python dictionaries to count activity events and commits per developer. This made HashMaps feel more useful because the data looked like something from GitHub.

### What confused me initially

Initially I only thought of HashMaps as interview problems. I did not immediately see how often they show up in analytics.

### How I figured it out

I wrote a small event counter for `COMMIT`, `PR_CREATED`, and `REVIEW`. Once I saw the frequency report, the pattern clicked.

### What I would improve next

I would add file input support so the analyzer can read logs from a `.txt` or `.csv` file.

## Day 4 - Recursion

### What I learned

Recursion started making more sense after I visualized the folder tree and dependency graph. The base case matters more than I first realized.

### What confused me initially

I kept getting confused about where execution returns after the recursive call finishes.

### How I figured it out

Drawing a recursion tree helped a lot. I also added a `visited` set in dependency traversal because repeated dependencies can cause duplicate work.

### What I would improve next

I want to try memoization or cycle detection with clearer error messages.

## Day 5 - SQL Joins and Analytics

### What I learned

I learned how joins connect separate parts of an engineering workflow. Developers write commits, authors open PRs, reviewers leave reviews, and repositories tie everything together.

### What confused me initially

At first I was unsure whether reviews should be stored inside the pull request table.

### How I figured it out

I decided to create a separate `reviews` table because a single PR can have multiple reviewers and multiple decisions. It makes queries slightly longer, but the design is easier to extend.

### What I would improve next

I would add a `ci_checks` table and write queries for build stability.

## Day 6 - Indexing and Transactions

### What I learned

Indexes are not just "make query fast" magic. They help reads but add cost when writing data. Transactions also felt clearer when I tied them to a pull request approval flow.

### What confused me initially

I was not sure which columns deserved indexes.

### How I figured it out

I looked at the joins and filters. Foreign keys like `developer_id`, `repository_id`, and `pr_id` made sense as index candidates.

### What I would improve next

I would run `EXPLAIN` plans on a real PostgreSQL database instead of only documenting the expected behavior.

## Day 7 - System Design and Review

### What I learned

I learned that system design is about explaining choices, not just listing components. The PDF reference helped me think about layers, queues, observability, and security.

### What confused me initially

The reference architecture was much bigger than my project. I was unsure how much of it to include without overengineering the Week-1 repo.

### How I figured it out

I adapted only the patterns that fit: webhook ingestion, async processing, cache, audit logs, RBAC, and monitoring. I left advanced sandbox execution as a future idea.

### What I would improve next

I would build a tiny working API that receives a fake GitHub event and updates analytics.

