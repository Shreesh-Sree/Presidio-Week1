# SDE Code Quality & Peer Review Checklist

This document guides developer reviews and branch integration requirements.

## 1. Local Code Standards
- **Style Consistency**: Python scripts must be formatted and linted (no syntax warnings).
- **Correct Data Structures**: Dictionaries used for $O(1)$ lookup operations, avoiding unnecessary $O(N)$ nested search loops.
- **Robust Exception Handling**: Database operations must run inside try/except blocks to rollback failed transactions.

---

## 2. GitHub Collaboration Rules
- **No Direct Commits**: Developers must work in short-lived feature branches (`feature/<description>`).
- **Required Pull Request Reviews**: Merges to the `main` branch require a PR with at least 1 approval.
- **Passing Status Checks**: CI verification workflows must pass before the branch is merged.
- **Branch Cleanup**: The source branch should be deleted after merging to keep the repository history tidy.
