# opencode-enterprise-python

Enterprise-grade Python project template with CI/CD, security scanning,
dependabot, and AI-powered code review.

## Enterprise Standards

| Practice | Tool | When |
|----------|------|------|
| SAST | Ruff + mypy | Every build |
| SCA | Dependabot + pip-audit | Weekly / every PR |
| Secret scan | Gitleaks | Every PR |
| Code review | Gemini AI | Every PR |
| SBOM | CycloneDX | Every release |

## Prerequisites

- Python 3.11+

## Quick Start

```bash
git clone https://github.com/Ya-wenWu/opencode-enterprise-python.git
cd opencode-enterprise-python
pip install -e ".[dev]"
pytest
```

## Project Structure

```
├── src/
│   └── my_app/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_greeting.py
├── pyproject.toml
├── .github/
│   └── workflows/
│       ├── ai-code-review.yml    # Gemini AI review on every PR
│       ├── ci.yml                 # Gitleaks + pip-audit + ruff + pytest
│       ├── dependency-review.yml  # Dependency graph check
│       └── release.yml            # SBOM + PyPI publish
├── .gitleaks.toml                 # Secret scanning rules
├── CONTRIBUTING.md                # Contribution guide
├── CODE_OF_CONDUCT.md             # Community guidelines
├── SECURITY.md                    # Security policies
└── LICENSE                        # MIT
```

## Security

This project uses multiple layers of security:

- **Gitleaks** scans every PR for hardcoded secrets
- **pip-audit** checks dependencies for known vulnerabilities
- **Dependabot** automatically opens PRs for outdated dependencies
- **Gemini AI** reviews every PR for security issues
- **Secret scanning + push protection** enabled at GitHub level
- **Branch ruleset** requires PR for all branches

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute.

## License

MIT
