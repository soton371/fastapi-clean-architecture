📂 Folder Structure

app/
│
├── main.py                  # Entry point
├── core/                    # Core config & utilities
│   ├── config.py             # Settings, environment variables
│   ├── security.py           # JWT, password hashing, OAuth utils
│   └── logging_config.py     # Logging setup
│
├── api/                     # API layer (routers, schemas, deps)
│   ├── dependencies.py       # Common dependencies
│   ├── v1/                   # Versioned APIs
│   │   ├── routes/           # Endpoint definitions
│   │   │   ├── user.py
│   │   │   ├── auth.py
│   │   │   └── ...
│   │   └── schemas/          # Pydantic models for requests/responses
│   │       ├── user.py
│   │       └── auth.py
│
├── services/                 # Business logic (use cases)
│   ├── user_service.py
│   └── auth_service.py
│
├── repositories/             # Data access layer
│   ├── user_repository.py
│   └── base.py
│
├── models/                   # SQLAlchemy ORM models
│   ├── user.py
│   └── __init__.py
│
├── db/                       # Database config
│   ├── session.py            # Session maker, engine
│   ├── migrations/           # Alembic migrations
│
└── tests/                    # Unit & integration tests
    ├── conftest.py
    ├── test_user.py
    └── test_auth.py
