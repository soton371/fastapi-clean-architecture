# FastAPI Clean Architecture Template

A production-grade FastAPI scaffold following Clean Architecture + light DDD.

## Quick Start

```bash
# 1) Create & activate venv (optional)
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install
pip install -r requirements.txt

# 3) Setup env
cp .env.example .env

# 4) Run DB (optional) — if you use Postgres via Docker
docker compose up -d

# 5) Run migrations (generate + apply if needed)
alembic upgrade head  # after initializing the DB

# 6) Start API
uvicorn app.main:app --reload
```

## Layout

```
app/
  core/            # settings, logging, security helpers
  api/             # routers, schemas, dependencies (HTTP layer)
    v1/
      routes/      # endpoint definitions
      schemas/     # Pydantic request/response models
  services/        # business logic (use-cases)
  repositories/    # DB access (SQLAlchemy)
  models/          # ORM models
  db/              # session + migrations
tests/             # pytest
```

## Notes
- Uses SQLAlchemy 2.x, Pydantic v2, Alembic, JWT (PyJWT) and passlib for hashing.
- Switch DB by editing `DATABASE_URL` in `.env` and `app/db/session.py` if needed.
