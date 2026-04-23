import sys
from pathlib import Path

# Добавляем путь, чтобы Python мог импортировать модули из папки src
sys.path.append(str(Path(__file__).parent.parent))
from src.cli import cli



if __name__ == '__main__':
    cli()