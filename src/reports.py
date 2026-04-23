from typing import List, Dict, Any
from src.base_report import Report

class ClickbaitReport(Report):
    """Отчёт о кликбейтных видео: ctr > 15 и retention_rate < 40."""

    name = 'clickbait'

    def filter_and_sort(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        filtered = [
            row for row in data
            if row.get('ctr', 0) > 15 and row.get('retention_rate', 100) < 40
        ]
        # Сортировка по убыванию CTR
        return sorted(filtered, key=lambda x: x.get('ctr', 0), reverse=True)


#Регистр доступных отчётов
AVAILABLE_REPORTS = {cls.name: cls() for cls in [ClickbaitReport]}