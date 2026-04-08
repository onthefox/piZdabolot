"""
Autogen — обработка намерений через DB (PostgreSQL через SQLAlchemy)
Создаёт/связывает/удаляет сущности, возвращает структурированный результат.
"""

from __future__ import annotations

from typing import Any

from backend.models import Entity, Link


def autogen_handle(parsed_intent: dict[str, Any], db) -> dict[str, Any]:
    """
    Обработчик намерений:
      - create: создать сущность
      - link: связать две сущности
      - delete: удалить сущность
      - query: найти сущность
      - evolve: зарезервировано для будущего расширения
    """
    action = parsed_intent.get("action", "unknown")
    result: dict[str, Any] = {"action": action}

    try:
        if action == "create":
            name = parsed_intent.get("entity", "").strip()
            if not name:
                return {"action": action, "error": "Имя сущности не указано"}
            existing = db.query(Entity).filter_by(name=name).first()
            if existing:
                return {"action": action, "exists": existing.to_dict()}
            entity = Entity(name=name)
            db.add(entity)
            db.commit()
            db.refresh(entity)
            result["created"] = entity.to_dict()

        elif action == "link":
            names = parsed_intent.get("entities", [])
            if len(names) != 2:
                return {"action": action, "error": "Нужно ровно 2 имени для связи"}
            src = db.query(Entity).filter_by(name=names[0]).first()
            tgt = db.query(Entity).filter_by(name=names[1]).first()
            if not src or not tgt:
                missing = []
                if not src:
                    missing.append(names[0])
                if not tgt:
                    missing.append(names[1])
                return {"action": action, "error": f"Сущность не найдена: {', '.join(missing)}"}
            # Проверка дубликата
            existing_link = (
                db.query(Link)
                .filter_by(source_id=src.id, target_id=tgt.id)
                .first()
            )
            if existing_link:
                return {"action": action, "exists": existing_link.to_dict()}
            link = Link(source_id=src.id, target_id=tgt.id)
            db.add(link)
            db.commit()
            db.refresh(link)
            result["created"] = {"id": link.id, "source": src.name, "target": tgt.name}

        elif action == "delete":
            name = parsed_intent.get("entity", "").strip()
            if not name:
                return {"action": action, "error": "Имя сущности не указано"}
            entity = db.query(Entity).filter_by(name=name).first()
            if not entity:
                return {"action": action, "error": f"Сущность '{name}' не найдена"}
            db.delete(entity)
            db.commit()
            result["deleted"] = name

        elif action == "query":
            name = parsed_intent.get("entity", "").strip()
            if not name:
                return {"action": action, "error": "Имя сущности не указано"}
            entity = db.query(Entity).filter_by(name=name).first()
            if not entity:
                return {"action": action, "error": f"Сущность '{name}' не найдена"}
            # Найти связи
            src_links = db.query(Link).filter_by(source_id=entity.id).all()
            tgt_links = db.query(Link).filter_by(target_id=entity.id).all()
            connections = []
            for lnk in src_links + tgt_links:
                other = db.query(Entity).filter_by(
                    id=lnk.target_id if lnk.source_id == entity.id else lnk.source_id
                ).first()
                if other:
                    connections.append(other.name)
            result["entity"] = entity.to_dict()
            result["connections"] = connections

        elif action == "evolve":
            # Зарезервировано для будущего LLM-расширения
            result["status"] = "not_implemented_yet"
            result["hint"] = "Эволюция требует LLM-интеграцию"

        else:
            result["result"] = "Неизвестное действие"
            result["hint"] = "Попробуйте: создать X, связать X и Y, найти X, удалить X"

    except Exception as exc:
        db.rollback()
        result["error"] = str(exc)

    return result
