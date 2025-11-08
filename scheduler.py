import schedule
import time
import datetime
import subprocess

subprocess.run([".\\venv\\Scripts\\python.exe", "main.py"], check=True)
def run_parser_job():
    print("Запуск main.py как отдельного процесса...")
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    # Вызываем main.py. Это гарантирует, что драйвер Chrome будет закрываться после каждого цикла.
    subprocess.run([".\\venv\\Scripts\\python.exe", "main.py"], check=True)

#schedule.every(1).hour.do(run_parser_job) # Каждый час
schedule.every(3).minutes.do(run_parser_job)
# schedule.every().day.at("10:30").do(run_parser_job) # Ежедневно в 10:30
while True:
    schedule.run_pending()
    time.sleep(1) # Ждем 1 секунду перед следующей проверкой    