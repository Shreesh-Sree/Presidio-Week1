# Continuous Integration & Delivery Guidelines

This document details the CI pipeline setup and policy rules for `Presidio-Week1`.

## 1. Automated Checks Workflow
Every pull request targeting `main` automatically runs verification jobs:
- **Code Linter**: Ensures files adhere to pep8 style rules.
- **Python Syntax Compile**: Compiles python files using `py_compile` to catch structural compile errors.

---

## 2. GitHub Actions Configuration
The pipeline is defined in `.github/workflows/ci.yml`.

```yaml
name: CI Verification

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
```

---

## 3. Branch Protections & Merge Requirements
- **Protected Branch**: Merges to `main` must use Pull Requests.
- **Required Reviews**: At least 1 review approval is required before branches are merged.
