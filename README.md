# Решение тестового задания по отчетам

## Запуск

1. Склонируйте репозиторий к себе на локальную машину
   ```
   git clone https://github.com/ErkinBabayakov/youtube_metrics.git
   ```
2. Перейдите в папку с проектом
   ```
   cd youtube_metrics/
   ```
4. При необходимости создайте и активируйте виртуальное окружение
   ```
   python -m venv venv
   ```
   - Активация на Windows
   ```
   venv\Scripts\activate
   ```
   - macOS/Linux
   ```
   source venv/bin/activate
   ```
5. Установите необходимые зависимости, из файла `requirements.txt` командой :
   ```
   pip install -r requirements.txt
   ```
6. Запустите скрипт командой:
   
   - Linux/macOS
   ```
    python3 src/main.py --files stats1.csv stats2.csv --report clickbait
   ```
   - Windows
   ```
   python src/main.py --files stats1.csv stats2.csv --report clickbait
   ```
   
