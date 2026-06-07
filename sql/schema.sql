CREATE TABLE developers (
    developer_id INTEGER PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    github_username VARCHAR(50) NOT NULL UNIQUE,
    team_name VARCHAR(50) NOT NULL,
    joined_on DATE NOT NULL
);

CREATE TABLE repositories (
    repository_id INTEGER PRIMARY KEY,
    repository_name VARCHAR(100) NOT NULL UNIQUE,
    owning_team VARCHAR(50) NOT NULL,
    created_on DATE NOT NULL
);

CREATE TABLE commits (
    commit_id INTEGER PRIMARY KEY,
    repository_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    commit_hash VARCHAR(40) NOT NULL UNIQUE,
    message VARCHAR(255) NOT NULL,
    lines_added INTEGER NOT NULL,
    lines_deleted INTEGER NOT NULL,
    committed_at TIMESTAMP NOT NULL,
    FOREIGN KEY (repository_id) REFERENCES repositories(repository_id),
    FOREIGN KEY (developer_id) REFERENCES developers(developer_id)
);

CREATE TABLE pull_requests (
    pr_id INTEGER PRIMARY KEY,
    repository_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('OPEN', 'APPROVED', 'MERGED', 'CLOSED')),
    created_at TIMESTAMP NOT NULL,
    merged_at TIMESTAMP,
    FOREIGN KEY (repository_id) REFERENCES repositories(repository_id),
    FOREIGN KEY (author_id) REFERENCES developers(developer_id)
);

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    pr_id INTEGER NOT NULL,
    reviewer_id INTEGER NOT NULL,
    decision VARCHAR(30) NOT NULL CHECK (decision IN ('COMMENTED', 'CHANGES_REQUESTED', 'APPROVED')),
    review_comment VARCHAR(255),
    reviewed_at TIMESTAMP NOT NULL,
    FOREIGN KEY (pr_id) REFERENCES pull_requests(pr_id),
    FOREIGN KEY (reviewer_id) REFERENCES developers(developer_id)
);

