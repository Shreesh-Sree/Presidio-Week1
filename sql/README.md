# SQL Developer Analytics

I used this folder to model a small developer productivity database. The goal was to make joins feel useful instead of writing random table examples.

## Tables

- `developers`: engineers contributing to repositories
- `repositories`: codebases owned by teams
- `commits`: code changes linked to developers and repositories
- `pull_requests`: reviewable units of work
- `reviews`: review decisions and comments

I considered storing review information directly in `pull_requests`, but that would break down once a PR has more than one reviewer. Keeping `reviews` separate adds joins, but the schema is cleaner.

## Files

- `schema.sql`: table definitions and constraints
- `sample_data.sql`: sample engineering workflow data
- `joins.sql`: analytics queries using joins, grouping, HAVING, and subqueries
- `indexing.md`: notes about indexes and B-Tree behavior
- `transactions.sql`: pull request approval transaction examples

## Questions I Tried to Answer

- Who is the most active developer?
- Which repository receives the most reviews?
- Who is the top contributor by line changes?
- What is the average number of reviews per pull request?
- Which developers review work authored by others?
- Which repositories have high commit volume?

## Notes

The query file includes `RIGHT JOIN` and `FULL JOIN`, which are supported by PostgreSQL. If I run this in SQLite later, I will need to rewrite those examples using `LEFT JOIN` and `UNION`.

## Lessons Learned

- SQL design becomes easier when the relationships are real.
- Joins are not just syntax; they represent product relationships.
- Indexes should come from query patterns, not guesses.

## TODO

- Add a `ci_checks` table.
- Test queries in PostgreSQL and include sample outputs.
- Add `EXPLAIN` screenshots or notes for indexed queries.

