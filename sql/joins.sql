-- 1. INNER JOIN: commits with developer and repository context.
SELECT d.full_name, r.repository_name, c.commit_hash, c.message
FROM commits c
INNER JOIN developers d ON c.developer_id = d.developer_id
INNER JOIN repositories r ON c.repository_id = r.repository_id;

-- 2. LEFT JOIN: all pull requests, including PRs without reviews.
SELECT pr.pr_id, pr.title, rv.review_id, rv.decision
FROM pull_requests pr
LEFT JOIN reviews rv ON pr.pr_id = rv.pr_id;

-- 3. RIGHT JOIN: all reviews matched to pull requests.
SELECT pr.title, rv.decision, rv.reviewed_at
FROM pull_requests pr
RIGHT JOIN reviews rv ON pr.pr_id = rv.pr_id;

-- 4. FULL JOIN: show developers and commits, including unmatched rows.
SELECT d.full_name, c.commit_hash
FROM developers d
FULL JOIN commits c ON d.developer_id = c.developer_id;

-- 5. Most active developer by commit count.
SELECT d.full_name, COUNT(c.commit_id) AS commit_count
FROM developers d
JOIN commits c ON d.developer_id = c.developer_id
GROUP BY d.full_name
ORDER BY commit_count DESC
LIMIT 1;

-- 6. Top contributor by total changed lines.
SELECT d.full_name, SUM(c.lines_added + c.lines_deleted) AS total_line_changes
FROM developers d
JOIN commits c ON d.developer_id = c.developer_id
GROUP BY d.full_name
ORDER BY total_line_changes DESC
LIMIT 1;

-- 7. Most reviewed repository.
SELECT r.repository_name, COUNT(rv.review_id) AS review_count
FROM repositories r
JOIN pull_requests pr ON r.repository_id = pr.repository_id
JOIN reviews rv ON pr.pr_id = rv.pr_id
GROUP BY r.repository_name
ORDER BY review_count DESC
LIMIT 1;

-- 8. Average reviews per PR.
SELECT AVG(review_count) AS average_reviews_per_pr
FROM (
    SELECT pr.pr_id, COUNT(rv.review_id) AS review_count
    FROM pull_requests pr
    LEFT JOIN reviews rv ON pr.pr_id = rv.pr_id
    GROUP BY pr.pr_id
) pr_review_counts;

-- 9. Repositories with more than two commits.
SELECT r.repository_name, COUNT(c.commit_id) AS commit_count
FROM repositories r
JOIN commits c ON r.repository_id = c.repository_id
GROUP BY r.repository_name
HAVING COUNT(c.commit_id) > 2;

-- 10. Developers who reviewed someone else's PR.
SELECT DISTINCT reviewer.full_name AS reviewer_name
FROM reviews rv
JOIN pull_requests pr ON rv.pr_id = pr.pr_id
JOIN developers reviewer ON rv.reviewer_id = reviewer.developer_id
WHERE rv.reviewer_id <> pr.author_id;

-- 11. Pull requests with more reviews than the average PR.
SELECT pr.pr_id, pr.title, COUNT(rv.review_id) AS review_count
FROM pull_requests pr
LEFT JOIN reviews rv ON pr.pr_id = rv.pr_id
GROUP BY pr.pr_id, pr.title
HAVING COUNT(rv.review_id) > (
    SELECT AVG(review_count)
    FROM (
        SELECT COUNT(review_id) AS review_count
        FROM reviews
        GROUP BY pr_id
    ) counts
);

-- 12. Developers with no authored pull requests.
SELECT d.full_name
FROM developers d
LEFT JOIN pull_requests pr ON d.developer_id = pr.author_id
WHERE pr.pr_id IS NULL;

-- 13. Open PRs with author and repository.
SELECT pr.title, d.full_name AS author, r.repository_name
FROM pull_requests pr
JOIN developers d ON pr.author_id = d.developer_id
JOIN repositories r ON pr.repository_id = r.repository_id
WHERE pr.status = 'OPEN';

-- 14. Review decision distribution.
SELECT decision, COUNT(*) AS decision_count
FROM reviews
GROUP BY decision
ORDER BY decision_count DESC;

-- 15. Repository productivity summary.
SELECT
    r.repository_name,
    COUNT(DISTINCT c.commit_id) AS commits,
    COUNT(DISTINCT pr.pr_id) AS pull_requests,
    COUNT(DISTINCT rv.review_id) AS reviews
FROM repositories r
LEFT JOIN commits c ON r.repository_id = c.repository_id
LEFT JOIN pull_requests pr ON r.repository_id = pr.repository_id
LEFT JOIN reviews rv ON pr.pr_id = rv.pr_id
GROUP BY r.repository_name;

-- 16. Developers above average commit count.
SELECT d.full_name, COUNT(c.commit_id) AS commit_count
FROM developers d
JOIN commits c ON d.developer_id = c.developer_id
GROUP BY d.full_name
HAVING COUNT(c.commit_id) > (
    SELECT AVG(commit_count)
    FROM (
        SELECT COUNT(*) AS commit_count
        FROM commits
        GROUP BY developer_id
    ) developer_commit_counts
);

