"""
SymbioCore — интерпретация намерений
Поддерживает: create, link, delete, query, evolve
"""

import re
from typing import Any


def interpret_intent(text: str) -> dict[str, Any]:
    """
    Примитивная интерпретация текстового намерения.
    Возвращает структурированный словарь с действием и параметрами.
    """
    if not text or not text.strip():
        return {"action": "unknown", "raw": "", "error": "Пустое намерение"}

    text = text.strip().lower()

    # Создать сущность
    m = re.match(r"^создать\s+(.+)$", text)
    if m:
        entity = m.group(1).strip()
        return {"action": "create", "entity": entity}

    # Связать сущности
    m = re.match(r"^связать\s+(.+?)\s+и\s+(.+)$", text)
    if m:
        return {"action": "link", "entities": [m.group(1).strip(), m.group(2).strip()]}

    # Удалить сущность
    m = re.match(r"^удалить\s+(.+)$", text)
    if m:
        return {"action": "delete", "entity": m.group(1).strip()}

    # Запрос информации
    m = re.match(r"^(?:найти|показать|что\s+такое)\s+(.+)$", text)
    if m:
        return {"action": "query", "entity": m.group(1).strip()}

    # Эволюция / расширить
    m = re.match(r"^(?:эволюция|расширить|развить)\s+(.+)$", text)
    if m:
        return {"action": "evolve", "entity": m.group(1).strip()}

    return {"action": "unknown", "raw": text}
