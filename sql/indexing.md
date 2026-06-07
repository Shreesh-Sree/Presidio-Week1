# Database Indexing

I initially understood indexes as "things that make queries faster." That is true, but incomplete. After looking at the joins in this project, I started thinking of indexes as shortcuts the database can use when filtering or joining large tables.

## Example

```sql
CREATE INDEX idx_developer
ON commits(developer_id);
```

This helps a query like:

```sql
SELECT *
FROM commits
WHERE developer_id = 1;
```

Without an index, the database may need to scan every commit row. With an index, it can find matching `developer_id` values more directly.

## B-Tree Notes

Most relational databases use B-Tree or B+Tree indexes for common lookups. My current understanding is:

- keys are stored in sorted order
- the tree stays balanced
- searching is usually closer to `O(log n)` than `O(n)`

This is still an area I want to explore more by running real `EXPLAIN` plans.

## Indexes I Would Add

```sql
CREATE INDEX idx_commits_developer
ON commits(developer_id);

CREATE INDEX idx_commits_repository
ON commits(repository_id);

CREATE INDEX idx_pull_requests_repository
ON pull_requests(repository_id);

CREATE INDEX idx_reviews_pr
ON reviews(pr_id);

CREATE INDEX idx_reviews_reviewer
ON reviews(reviewer_id);
```

I chose these because they appear often in joins and filters.

## Tradeoffs

Indexes are not free. They take storage, and writes become a little more expensive because the database has to update the index too.

For this Week-1 project, I am documenting the index choices. In a real project, I would confirm them using query plans and actual data volume.

## TODO

- Run `EXPLAIN ANALYZE` in PostgreSQL.
- Compare query plans before and after adding indexes.
- Add indexes for timestamp filters if dashboard queries use date ranges often.

