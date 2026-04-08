"""
SymbioHive — примитивная graph-абстракция в памяти (для прототипов)
Точки расширения:
  - заменить списки на PostgreSQL/Neo4j
  - добавить типы сущностей и связей
  - добавить мета-данные (тэги, веса, временные метки)
"""

from typing import Any

entities: list[dict[str, Any]] = []
links: list[dict[str, Any]] = []
_next_entity_id = 1
_next_link_id = 1


def create_entity(name: str) -> dict[str, Any]:
    """Создать сущность. Если имя уже существует — вернуть существующую."""
    global _next_entity_id
    existing = next((e for e in entities if e["name"].lower() == name.lower()), None)
    if existing:
        return existing
    e = {"id": _next_entity_id, "name": name, "meta": {}}
    entities.append(e)
    _next_entity_id += 1
    return e


def link_entities(source_name: str, target_name: str) -> dict[str, Any] | None:
    """Создать связь между двумя сущностями по именам."""
    global _next_link_id
    src = next((e for e in entities if e["name"].lower() == source_name.lower()), None)
    tgt = next((e for e in entities if e["name"].lower() == target_name.lower()), None)
    if not src or not tgt:
        return None
    # Проверка дубликата
    existing = next(
        (l for l in links if l["source"] == src["id"] and l["target"] == tgt["id"]),
        None,
    )
    if existing:
        return existing
    lnk = {"id": _next_link_id, "source": src["id"], "target": tgt["id"], "meta": {}}
    links.append(lnk)
    _next_link_id += 1
    return lnk


def get_entities() -> list[dict[str, Any]]:
    """Вернуть копию списка сущностей."""
    return list(entities)


def get_links() -> list[dict[str, Any]]:
    """Вернуть копию списка связей."""
    return list(links)


def delete_entity(name: str) -> bool:
    """Удалить сущность и все её связи."""
    global _next_entity_id
    idx = next((i for i, e in enumerate(entities) if e["name"].lower() == name.lower()), None)
    if idx is None:
        return False
    entity_id = entities[idx]["id"]
    entities.pop(idx)
    # Удалить связанные рёбра
    links[:] = [l for l in links if l["source"] != entity_id and l["target"] != entity_id]
    return True


def stats() -> dict[str, int]:
    """Статистика экосистемы."""
    return {"entities": len(entities), "links": len(links)}
