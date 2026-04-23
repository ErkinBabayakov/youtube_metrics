from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Report(ABC):
    """Базовый класс для всех отчётов."""

    @abstractmethod
    def filter_and_sort(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Применяет фильтрацию и сортировку к данным."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Имя отчёта, которое используется в --report."""
        pass

    @property
    def columns(self) -> List[str]:
        """Колонки для вывода (по умолчанию title, ctr, retention_rate)."""
        return ['title', 'ctr', 'retention_rate']