# Project Name

<!-- Describe your project in 2-3 sentences -->

## Prerequisites

- Python 3.11+

## Quick Start

```bash
git clone <repo-url>
cd <repo-name>
pip install -e ".[dev]"
pytest
```

## Enterprise Standards

| Practice | Tool | When |
|----------|------|------|
| SAST | Ruff + mypy | Every build |
| SCA | Dependabot + pip-audit | Weekly / every PR |
| Secret scan | Gitleaks | Every PR |
| Code review | Gemini AI | Every PR |
| SBOM | CycloneDX | Every release |

## License

MIT
