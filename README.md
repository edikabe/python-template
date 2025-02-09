# Lambda Project

A Python AWS Lambda project using hexagonal architecture.

## Project Structure

```
├── src/
│   ├── application/        # Application layer (use cases)
│   │   ├── ports/         # Input/output ports (interfaces)
│   │   └── services.py    # Use case implementations
│   ├── domain/            # Domain layer (business logic)
│   │   └── models.py      # Domain models
│   ├── infrastructure/    # Infrastructure layer
│   │   └── repositories/  # Repository implementations
│   └── lambda_function.py # AWS Lambda handler
├── tests/                 # Test files
├── pyproject.toml        # Project configuration
└── README.md
```

## Setup

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

## Development

- Run tests:
```bash
poetry run pytest
```

- Type checking:
```bash
poetry run mypy src tests
```

- Linting:
```bash
poetry run ruff check .
```

## Architecture

This project follows hexagonal architecture (ports and adapters) pattern:

- **Domain Layer**: Contains business logic and domain models
- **Application Layer**: Contains use cases and port interfaces
- **Infrastructure Layer**: Contains concrete implementations of ports

## Testing

- Unit tests are written using pytest
- Mock repository is provided for testing
- Coverage reports are generated using pytest-cov