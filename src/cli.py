import argparse

from pathlib import Path
from tabulate import tabulate

from src.readers import read_metrics
from src.reports import AVAILABLE_REPORTS

def cli():
    parser = argparse.ArgumentParser(description='Анализ метрик YouTube видео.')
    parser.add_argument('--files', nargs='+', required=True,
                        help='Пути к CSV-файлам с метриками')
    parser.add_argument('--report', required=True,
                        choices=AVAILABLE_REPORTS.keys(),
                        help='Тип отчёта')
    args = parser.parse_args()

    report = AVAILABLE_REPORTS[args.report]

    # Сбор данных из всех переданных файлов
    all_data = []
    for file_path in args.files:
        try:
            for row in read_metrics(Path(file_path)):
                all_data.append(row)
        except FileNotFoundError:
            print(f"Ошибка: файл не найден - {file_path}")
            return
        except Exception as e:
            print(f"Ошибка при чтении {file_path}: {e}")
            return

    if not all_data:
        print("Нет данных для анализа.")
        return

    result = report.filter_and_sort(all_data)

    if not result:
        print("Видео, удовлетворяющих условиям, не найдено.")
        return

    # Подготовка таблицы
    table_data = [[row[col] for col in report.columns] for row in result]
    headers = report.columns
    print(tabulate(table_data, headers=headers, floatfmt=".2f", tablefmt="grid"))