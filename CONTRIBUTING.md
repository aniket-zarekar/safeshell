# Contributing Guide

This document defines the expected workflow for contributing to SafeShell and related agent/tooling work.

## 1. Understand the project goals

Before contributing, understand the repository's purpose:

- protect shell execution from unsafe or destructive commands
- keep command evaluation transparent and explainable
- support safe automation and developer tooling

## 2. Keep repository scope focused

Maintain clear boundaries between:

- agent logic
- tooling utilities
- templates
- infrastructure or workflow configuration

Avoid mixing unrelated concerns in the same contribution.

## 3. Start from the repository structure

The repository is organized into these top-level areas:

- `agents/` for agent-oriented implementations
- `tools/` for MCP servers, utilities, and development helpers
- `template/` for reusable starter files
- `.github/` for PR and workflow templates

## 4. Review the contribution entry points

Use the relevant area as the entry point for your work:

- new autonomous workflows -> `agents/`
- new developer utilities -> `tools/`
- new project starter files -> `template/`
- process and review updates -> `.github/`

## 5. Follow naming conventions

Use descriptive, lowercase names for directories and files when possible.

Examples:

- `agents/guard-agent/`
- `tools/safety-checker/`
- `template/README.md`

## 6. Document before coding

For any significant addition:

- describe the problem
- define expected behavior
- document setup requirements
- document security considerations

## 7. Keep changes small and reviewable

Prefer focused changes over large sweeping edits. Small PRs are easier to review and validate.

## 8. Validate before submission

When relevant, test the added behavior locally and include:

- setup steps
- expected output
- validation notes

## 9. Protect secrets and local configuration

Never commit:

- API keys
- tokens
- credentials
- environment secrets

Use `.env.example` and sanitized examples instead.

## 10. Use templates consistently

When creating a new contribution, begin from the standard templates in `template/`.

## 11. Write maintainable documentation

Every new module should include:

- purpose
- setup instructions
- usage examples
- limitations or constraints

## 12. Submit a clean pull request

Before opening a PR:

- ensure the branch is up to date
- provide a clear summary
- explain the motivation
- document validation performed
- mention any follow-up work needed

## Pull request checklist

- [ ] I read the project README and contribution guide.
- [ ] My change matches the repository structure.
- [ ] I did not commit secrets or sensitive files.
- [ ] I documented setup and usage where needed.
- [ ] I validated the change locally where possible.
- [ ] My PR description clearly explains the change.

## Contributor expectations

Be respectful, precise, and safety-aware. The project emphasizes transparent, responsible shell safety design, and contributors should carry that philosophy into their work.
