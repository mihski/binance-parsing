import platform
import re
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def get_chrome_version_and_puth() -> str:
    """Определяет версию Chrome для Windows, Linux или macOS."""
    system = platform.system()


    if system == "Linux":
        chrome_binaries = [
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/usr/bin/chromium",
            "/usr/bin/chromium-browser",
            "/snap/bin/chromium"
        ]

        chrome_path = None
        for binary in chrome_binaries:
            try:
                output = subprocess.check_output([binary, "--version"],
                stderr=subprocess.STDOUT, text=True)
                match = re.search(r"\d+\.\d+\.\d+\.\d+", output)
                if match:
        # Нашли и путь, и версию
                    chrome_path = binary
                    return match.group(0), chrome_path
            except (FileNotFoundError, subprocess.CalledProcessError):
                continue
        return None, None # Если ничего не найдено

    elif system == "Windows" :
        import winreg

        paths = [
            r"SOFTWARE\Google\Chrome\BLBeacon",
            r"SOFTWARE\WOW6432Node\Google\Chrome\BLBeacon"
        ]

        for reg_path in paths:
            #  ищем ключ для определения версии
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
                chrome_version, _ = winreg.QueryValueEx(key, "version")
                print("находим версию")
                break

            except FileNotFoundError:
                continue

        path_commands = [
            r"SOFTWARE\Clients\StartMenuInternet\Google Chrome\shell\open\command",
            r"SOFTWARE\WOW6432Node\Clients\StartMenuInternet\Google Chrome\shell\open\command"
        ]

        for cmd_path in path_commands:
             #  ищем ключ для определения пути к браущеру
            try:
                # Ищем в HKEY_LOCAL_MACHINE, так как это общесистемная установка
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cmd_path)

                # Получаем команду запуска (например: "C:\...\chrome.exe" --profile-directory=Default)
                command, _ = winreg.QueryValueEx(key, None) # None = (Default) value

                # Используем regex, чтобы извлечь только путь в кавычках
                match = re.search(r'"([^"]*chrome.exe)"', command)
                if match:
                    chrome_path = match.group(1) # Получаем путь без кавычек
                    print("находим путь")
                    return chrome_version,chrome_path
                    break
            except FileNotFoundError:
                continue

    return None, None # Если ничего не найдено

def get_chrome_driver(headless: bool = True):
    """Создаёт и возвращает готовый WebDriver с учётом версии Chrome."""

    options = webdriver.ChromeOptions()
    chrome_version,chrome_path = get_chrome_version_and_puth()
    options.binary_location = chrome_path
    if not chrome_version:
        raise RuntimeError("Не удалось определить версию Chrome.")

    print(f"🧭 Найдена версия Chrome: {chrome_version}")

    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager(driver_version=chrome_version).install())
    driver = webdriver.Chrome(service=service, options=options)
    print(F"✅ WebDriver версии {chrome_version} успешно создан.")
    return driver

# if __name__== "__main__":

#     get_chrome_driver()


