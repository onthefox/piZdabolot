"""
SymbioHive — живая экосистема: онтология, сущности, связи
"""

from .hive import create_entity, link_entities, get_entities, get_links, delete_entity, stats

__all__ = ["create_entity", "link_entities", "get_entities", "get_links", "delete_entity", "stats"]
