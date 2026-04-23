import tempfile
import sys

from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.readers import read_metrics

def test_read_metrics():
    content = """title,ctr,retention_rate,views
Видео 1,15.5,45.2,1000
Видео 2,22.0,30.1,2000
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    rows = list(read_metrics(temp_path))
    assert len(rows) == 2
    assert rows[0]['title'] == 'Видео 1'
    assert rows[0]['ctr'] == 15.5
    assert rows[0]['retention_rate'] == 45.2
    assert rows[1]['ctr'] == 22.0
    temp_path.unlink()

def test_read_metrics_invalid_data():
    content = """title,ctr,retention_rate
Bad,abc,30.0
Good,20.0,40.0
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    rows = list(read_metrics(temp_path))
    assert len(rows) == 1  # только вторая строка
    assert rows[0]['title'] == 'Good'
    temp_path.unlink()