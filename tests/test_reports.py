import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.reports import ClickbaitReport

@pytest.fixture
def sample_data():
    return [
        {'title': 'A', 'ctr': 20.0, 'retention_rate': 35.0},
        {'title': 'B', 'ctr': 10.0, 'retention_rate': 30.0},  # ctr низкий
        {'title': 'C', 'ctr': 18.0, 'retention_rate': 50.0},  # удержание высокое
        {'title': 'D', 'ctr': 25.0, 'retention_rate': 20.0},
        {'title': 'E', 'ctr': 16.0, 'retention_rate': 39.0},
    ]

def test_clickbait_filter(sample_data):
    report = ClickbaitReport()
    result = report.filter_and_sort(sample_data)
    titles = [row['title'] for row in result]
    # Должны попасть A, D, E (ctr > 15 и retention < 40)
    assert titles == ['D', 'A', 'E']  # сортировка по убыванию ctr: 25, 20, 16
    assert result[0]['ctr'] == 25.0
    assert result[1]['ctr'] == 20.0
    assert result[2]['ctr'] == 16.0

def test_clickbait_empty():
    data = [{'title': 'X', 'ctr': 14.0, 'retention_rate': 39.0}]
    report = ClickbaitReport()
    assert report.filter_and_sort(data) == []