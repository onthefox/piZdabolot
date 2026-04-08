# Contributing

Thank you for your interest in contributing to Adapt SymbioSystem!

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Make changes
4. Test locally: `make up` or `make backend` + `make frontend`
5. Commit with descriptive message
6. Push and open a Pull Request

## Code Standards

- **Python 3.11+** — Use modern type hints
- **Type hints** — All public functions must be typed
- **Docstrings** — Document all public classes and methods
- **Line length** — 100 characters max

## Running Tests

```bash
# Full stack with Docker
make up

# Backend only
make backend

# Frontend only
make frontend

# Run migrations
make migrate
```

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new capability
fix: resolve a bug
docs: update documentation
refactor: restructure code
test: add or update tests
ci: update CI/CD configuration
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
