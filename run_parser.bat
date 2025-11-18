@echo on
echo Переход в рабочую директорию...
cd /d "E:\Python\binance-parsing"
echo

echo Запуск скрипта...
REM Используем полный путь до интерпретатора Python внутри venv
E:\Python\binance-parsing\venv\Scripts\python.exe main.py

echo Скрипт Python завершил работу.
echo
PAUSE