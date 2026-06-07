-- Pull Request Approval Transaction Workflow
-- Scenario: create a PR, assign reviewer through a review row, approve it, then commit.

BEGIN;

INSERT INTO pull_requests (
    pr_id,
    repository_id,
    author_id,
    title,
    status,
    created_at,
    merged_at
) VALUES (
    6,
    1,
    2,
    'Add deployment event tracking',
    'OPEN',
    '2026-06-06 10:00:00',
    NULL
);

INSERT INTO reviews (
    review_id,
    pr_id,
    reviewer_id,
    decision,
    review_comment,
    reviewed_at
) VALUES (
    8,
    6,
    1,
    'APPROVED',
    'Deployment tracking is scoped and observable.',
    '2026-06-06 11:30:00'
);

UPDATE pull_requests
SET status = 'APPROVED'
WHERE pr_id = 6;

COMMIT;

-- Rollback scenario: reviewer requests changes, so the approval workflow is not finalized.

BEGIN;

INSERT INTO pull_requests (
    pr_id,
    repository_id,
    author_id,
    title,
    status,
    created_at,
    merged_at
) VALUES (
    7,
    2,
    5,
    'Add experimental productivity score',
    'OPEN',
    '2026-06-06 13:00:00',
    NULL
);

INSERT INTO reviews (
    review_id,
    pr_id,
    reviewer_id,
    decision,
    review_comment,
    reviewed_at
) VALUES (
    9,
    7,
    3,
    'CHANGES_REQUESTED',
    'Score formula needs clearer weighting and validation.',
    '2026-06-06 14:20:00'
);

-- The review failed approval criteria, so discard this transaction.
ROLLBACK;

