# Version Update Records

| Date | Name | Summary | Author | Notes |
|------|------|---------|--------|-------|
| 2026-06-10 | Initial | Enterprise repo template created | opencode | Base template for all Python projects |
| 2026-06-10 | Sample Project | Added sample module (my_app) + pytest + fixed code_review.py ruff issues | opencode | Includes greeting function, test, pyproject.toml dev deps |
| 2026-06-12 | AI Review Groq Fallback | Rewrote AI review with Gemini → NVIDIA → Groq triple fallback | opencode | Replaced opencode action with Python script; actions/checkout v4→v6; GROQ_API_KEY secret; ruleset narrowed to main only |
| 2026-06-12 | Security Fixes | Add .gitleaks.toml; fix SECURITY.md to use private reporting | opencode | Custom secret patterns; private vulnerability reporting instead of public issues |
