"""
SymbioFlow — обработка намерений
Принимает текст → интерпретирует через SymbioCore → выполняет через autogen
"""

from core.symbio_core import interpret_intent
from engine.autogen import autogen_handle


def handle_intent(text: str, db) -> dict:
    """
    Полный цикл: текст → парсинг → выполнение → результат.
    """
    parsed = interpret_intent(text)
    result = autogen_handle(parsed, db)
    result["intent"] = parsed
    return result
