# SymbioSystem — Симбиотическая AI-Экосистема

> **Не просто Neovim-плагин** — это полноценная симбиотическая AI-экосистема, где Neovim — лишь один из интерфейсов.

[![CI](https://github.com/onthefox/piZdabolot/actions/workflows/ci.yml/badge.svg)](https://github.com/onthefox/piZdabolot/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](docker-compose.yml)

---

## 🧩 Что это

**SymbioSystem** — это автономная симбиотическая экосистема нового поколения, которая:

- **Интерпретирует намерения** — превращает текстовые запросы в действия
- **Строит онтологию** — создаёт сущности, связи, эволюционирует
- **Автономно действует** — пайплайн: намерение → план → выполнение
- **Автогенерирует** — создаёт новые модули и расширяет систему
- **Визуализирует** — живой граф смыслов в реальном времени

Это **ядро AI-стартапа**, готовое к подаче в **Microsoft Founders Hub** и **GitHub for Startups**.

---

## 🏗️ Архитектура

```
piZdabolot (SymbioSystem MVP)
├── core/
│   ├── symbio_core/     # Ядро: интерпретация намерений (rules.py)
│   └── symbio_hive/     # Рой: онтология, сущности, связи (hive.py)
├── engine/
│   ├── symbio_flow/     # Движок: приём → план → выполнение (flow.py)
│   └── autogen/         # Автоген: создание сущностей/связей/модулей
├── backend/             # FastAPI + SQLAlchemy + PostgreSQL
│   ├── main.py          # 7 REST эндпоинтов
│   ├── models.py        # ORM: Entity, Link
│   └── db.py            # PostgreSQL подключение
├── ui/mind_palace/      # React + d3.js визуализация графа
│   ├── src/App.jsx      # Дашборд
│   ├── src/Graph.jsx    # Force-directed граф (d3.js)
│   └── src/EntityCard.jsx # Карточка сущности
├── meta/revolution/     # Roadmap, сценарии, истории
└── docker-compose.yml   # Полный стек одним командой
```

### Компоненты

| Компонент | Назначение | Статус |
|-----------|-----------|--------|
| **SymbioCore** | Интерпретация намерений (parse → структурировать) | ✅ MVP |
| **SymbioHive** | Живая экосистема: онтология, сущности, связи | ✅ MVP |
| **SymbioFlow** | Автономный движок: приём → план → выполнение | ✅ MVP |
| **Autogen** | Автогенерация сущностей и связей по тексту | ✅ MVP |
| **Backend** | FastAPI (7 endpoints) + PostgreSQL | ✅ MVP |
| **MindPalace UI** | React + d3.js force-directed граф | ✅ MVP |

---

## 🚀 Быстрый старт

### Docker (рекомендуется)

```bash
# Поднять весь стек
make up

# Или напрямую
docker-compose up --build
```

Откройте:
- **API Docs**: http://localhost:8000/docs
- **MindPalace UI**: http://localhost:3000

### Локальная разработка

```bash
# Бэкенд
cd backend
pip install -r requirements.txt
make backend   # uvicorn --reload на :8000

# Фронтенд (в другом терминале)
make frontend  # npm install + npm start на :3000
```

### Полезные команды

```bash
make down      # Остановить и удалить volumes
make migrate   # Инициализировать БД
make clean     # Полная очистка
```

---

## 🔌 API

| Method | Path | Описание |
|--------|------|----------|
| `POST` | `/intent` | Обработать текстовое намерение |
| `GET` | `/entities` | Список всех сущностей |
| `GET` | `/links` | Список всех связей |
| `POST` | `/entity` | Создать сущность напрямую |
| `POST` | `/link` | Создать связь напрямую |
| `GET` | `/stats` | Статистика экосистемы |
| `GET` | `/health` | Health check |

### Пример: отправка намерения

```bash
curl -X POST http://localhost:8000/intent \
  -H "Content-Type: application/json" \
  -d '{"intent": "создать Проект Адаптация"}'
```

Ответ:
```json
{
  "action": "create",
  "created": { "id": 1, "name": "Проект Адаптация" }
}
```

---

## 🎯 Позиционирование

**SymbioSystem — это не плагин для Neovim.** Это:

1. **AI-экосистема** — автономная система, которая интерпретирует намерения и действует
2. **Смысловой граф** — живая онтология, которая растёт и эволюционирует
3. **Платформа** — Neovim — лишь один из интерфейсов; API открыт для любых интеграций
4. **Стартап-продукт** — готов к подаче в Microsoft Founders Hub / GitHub for Startups

### Почему это важно

| Проблема | Решение SymbioSystem |
|----------|---------------------|
| AI-ассистенты — одноразовые запросы | Симбиотическая экосистема с памятью |
| Нет визуализации связей | MindPalace: живой граф смыслов |
| Статические онтологии | Растущая, эволюционирующая онтология |
| Нет автономности | Автономный движок: намерение → действие |

---

## 📊 Демо

### MindPalace UI

> 🎬 **GIF/видео скоро будет** — запишем после запуска `docker-compose up`

### API в действии

```bash
# Создать сущность
curl -X POST "http://localhost:8000/intent" \
  -H "Content-Type: application/json" \
  -d '{"intent": "создать Проект SymbioSystem"}'

# Связать сущности
curl -X POST "http://localhost:8000/intent" \
  -H "Content-Type: application/json" \
  -d '{"intent": "связать SymbioSystem и piZdabolot"}'

# Посмотреть граф
curl http://localhost:8000/entities
curl http://localhost:8000/links
```

---

## 🛠️ Технологический стек

- **Backend**: Python 3.11+ · FastAPI · SQLAlchemy · PostgreSQL 15
- **Frontend**: React 18 · d3.js (force-directed graph) · Axios
- **Инфраструктура**: Docker · docker-compose · GitHub Actions CI
- **Тестирование**: CI с PostgreSQL сервисом + Docker build проверка

---

## 📅 Roadmap

### ✅ Q2 2026 — MVP (текущий)
- [x] SymbioCore v1 — интерпретация намерений
- [x] SymbioHive — онтология и связи
- [x] SymbioFlow — автономный пайплайн
- [x] Autogen — автогенерация
- [x] FastAPI backend (7 endpoints)
- [x] MindPalace UI (React + d3.js)
- [x] Docker + docker-compose
- [x] CI pipeline

### 🚧 Q3 2026 — Автономные агенты
- [ ] SymbioFlow autonomous agents
- [ ] Multi-agent coordination
- [ ] Real-time WebSocket updates
- [ ] Entity cards с деталями
- [ ] LLM-powered intent parsing

### 📋 Q4 2026 — MindPalace 2.0
- [ ] Интерактивный граф с фильтрами
- [ ] Временная шкала эволюции
- [ ] Экспорт/импорт онтологии
- [ ] Плагины для VS Code, JetBrains
- [ ] API rate limiting + auth

### 🔮 Q1 2027 — SymbioSystem Cloud
- [ ] Managed SymbioSystem сервис
- [ ] Multi-tenant архитектура
- [ ] Billing + quotas
- [ ] SymbioSystem Marketplace
- [ ] Community-driven ontology

Полный roadmap: [`meta/revolution/ROADMAP.md`](meta/revolution/ROADMAP.md)

---

## 📄 Лицензии

| Компонент | Лицензия |
|-----------|----------|
| Всё | MIT © OnTheFox 2026 |

---

## 🤝 Вклад

Мы принимаем contributions! См. [`CONTRIBUTING.md`](CONTRIBUTING.md)

Кратко:
1. Fork → feature branch → PR
2. Тесты должны проходить (`make up`)
3. Conventional Commits

---

## 📞 Контакты

- **Репозиторий**: https://github.com/onthefox/piZdabolot
- **Issues**: https://github.com/onthefox/piZdabolot/issues
- **Автор**: OnTheFox
