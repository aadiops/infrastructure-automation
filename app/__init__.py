repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict

  - repo: local
    hooks:
      - id: python-format
        name: Python formatting
        entry: python -m black app
        language: system
        files: \.(py)$
