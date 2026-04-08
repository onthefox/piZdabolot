# Демо SymbioSystem — Инструкция по записи

## Цель
Создать 15-30 секундный GIF/видео демонстрации MindPalace UI для README и Founders Hub.

---

## 📹 Шаг 1: Запуск локального стека

```bash
# В корне проекта
make up

# Дождись запуска всех сервисов:
# - PostgreSQL: localhost:5432
# - Backend API: localhost:8000
# - MindPalace UI: localhost:3000
```

Откройте http://localhost:3000 в браузере.

---

## 🎬 Шаг 2: Сценарий демо (15-30 секунд)

### Кадры для записи:

**Кадр 1 (3 сек): Пустой граф**
- Покажите начальный экран MindPalace UI
- Подсветите надпись "Нет задач — добавьте первую!"

**Кадр 2 (5 сек): Создание сущности**
- Откройте терминал или Swagger UI (http://localhost:8000/docs)
- Выполните: `POST /intent` с телом `{"intent": "создать Проект Адаптация"}`
- Покажите ответ JSON с `created`

**Кадр 3 (5 сек): Создание второй сущности**
- `POST /intent` с `{"intent": "создать Сущность Экосистема"}`
- Покажите ответ

**Кадр 4 (5 сек): Связывание**
- `POST /intent` с `{"intent": "связать Проект Адаптация и Сущность Экосистема"}`
- Покажите ответ с `connections`

**Кадр 5 (5 сек): Визуализация графа**
- Вернитесь на MindPalace UI (localhost:3000)
- Обновите страницу
- Покажите граф с двумя узлами и связью
- Потяните узлы мышкой — покажите interactivity

**Кадр 6 (3 сек): Статистика**
- `GET /stats`
- Покажите `{"entities": 2, "links": 1}`

---

## 🛠️ Шаг 3: Инструменты записи

### macOS
```bash
# LICEcap (бесплатный, простой)
brew install licecap

# Или Gifski
brew install --cask gifski
```

### Linux
```bash
# Peek (простой рекордер GIF)
sudo apt install peek

# Или Byzanz
sudo apt install byzanz
byzanz-record --duration=30 --delay=2 demo.gif
```

### Windows
```
# ShareX (бесплатный)
https://getsharex.com/
```

### Chrome DevTools (альтернатива)
1. Откройте DevTools → Command Menu (Cmd+Shift+P)
2. Введите "Capture screenshot" или "Record screencast"
3. Экспортируйте как GIF

---

## ✂️ Шаг 4: Обрезка и оптимизация

```bash
# Сжать GIF (уменьшить размер)
gifsicle -O3 --colors 128 demo.gif > demo-optimized.gif

# Или онлайн: https://ezgif.com/optimize
```

**Целевой размер:** <2MB для README

---

## 📤 Шаг 5: Добавление в README

1. Загрузите GIF в GitHub issue или imgur
2. Вставьте в README:

```markdown
![SymbioSystem Demo](https://user-images.githubusercontent.com/USER/REPO/demo.gif)
```

---

## 🎯 Альтернатива: Скриншоты

Если GIF невозможен, минимум 3 скриншота:

1. **Пустой MindPalace** — начальный экран
2. **Граф с сущностями** — 2+ узла, связи
3. **Swagger UI** — API docs с примерами

Скриншоты: `cmd+shift+4` (macOS) или `gnome-screenshot` (Linux)
