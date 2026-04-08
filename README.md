# Adapt SymbioSystem — piZdabolot

> Симбиотическая экосистема нового поколения с автономным движком, живой смысловой средой и визуальным интерфейсом.

## Overview

Adapt SymbioSystem — это монорепозиторий с полностью рабочим MVP для симбиотической AI-экосистемы:

- **SymbioCore** — ядро интерпретации намерений (parse →结构化)
- **SymbioHive** — живая экосистема: онтология, сущности, связи
- **SymbioFlow** — автономный движок: приём намерения → план → выполнение
- **Autogen** — автогенерация сущностей и связей по тексту
- **MindPalace UI** — React + d3.js визуализация графа смыслов

## Quick Start

```bash
# Install & run with Docker
make up

# Or run locally
pip install -r backend/requirements.txt
make backend   # starts FastAPI on :8000
make frontend  # starts MindPalace on :3000
```

Open http://localhost:8000/docs for API docs, http://localhost:3000 for MindPalace UI.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/intent` | Process text intent → parse → execute |
| GET | `/entities` | List all entities |
| GET | `/links` | List all links |
| POST | `/entity` | Create entity directly |
| POST | `/link` | Create link directly |
| GET | `/stats` | Ecosystem statistics |
| GET | `/health` | Health check |

## Architecture

```
core/
├── symbio_core/     # Intent interpretation (rules.py)
└── symbio_hive/     # Entity & link management (hive.py)
engine/
├── symbio_flow/     # Intent → parse → execute pipeline
└── autogen/         # Auto-generation of entities/links
backend/
├── main.py          # FastAPI server (7 endpoints)
├── models.py        # SQLAlchemy ORM (Entity, Link)
└── db.py            # PostgreSQL connection
ui/mind_palace/
├── src/App.jsx      # React dashboard
├── src/Graph.jsx    # d3.js force-directed graph
└── src/EntityCard.jsx # Entity detail card
meta/revolution/     # Roadmap, stories, use cases
```

## Tech Stack

- **Backend**: Python 3.11 + FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React 18 + d3.js (force-directed graph)
- **Infrastructure**: Docker + docker-compose
- **CI**: GitHub Actions (backend tests + Docker build)

## License

MIT — OnTheFox 2026
