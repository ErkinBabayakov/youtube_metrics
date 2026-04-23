import csv
from pathlib import Path
from typing import Iterator, Dict, Any

def read_metrics(file_path: Path) -> Iterator[Dict[str, Any]]:
    """
    Читаем CSV-файл с метриками и возвращаем итератор словарей
    """
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #Пробуем преобразовать в числовые значения:
            try:
                row['ctr'] = float(row['ctr'])
                row['retention_rate'] = float(row['retention_rate'])
            except (KeyError, ValueError):
                #если строки с некорректными данными то пропускаем
                continue
            yield row