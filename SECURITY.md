# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | ✅        |

## Reporting a Vulnerability

Please report security vulnerabilities by opening an issue with the `security` label.

Do NOT post sensitive information (API keys, credentials, tokens) in public issues.

## Security Considerations

- **No hardcoded credentials** — All secrets via environment variables
- **PostgreSQL password** — Default `symbio` should be changed in production
- **CORS** — FastAPI allows all origins by default; restrict in production
- **Input validation** — Pydantic schemas validate all API inputs
- **SQL injection** — SQLAlchemy ORM prevents raw SQL injection

## Production Checklist

- [ ] Change default PostgreSQL password
- [ ] Set CORS allowed origins
- [ ] Enable HTTPS
- [ ] Set up rate limiting
- [ ] Add authentication layer
- [ ] Enable database encryption at rest
- [ ] Set up monitoring and alerting
