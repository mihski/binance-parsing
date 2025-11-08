"""
нахождение и загрузка вебдрайвера
"""
import re
import platform
import subprocess
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def get_chrome_version() -> str:
    """Определяет версию Chrome для Windows, Linux или macOS."""
    system = platform.system()

    try:
        if system == "Windows":
            import winreg # pylint: disable=import-outside-toplevel
            paths = [
                r"SOFTWARE\Google\Chrome\BLBeacon",
                r"SOFTWARE\WOW6432Node\Google\Chrome\BLBeacon"
            ]
            for reg_path in paths:
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
                    version, _ = winreg.QueryValueEx(key, "version")
                    return version
                except FileNotFoundError:
                    continue

        elif system == "Linux":
            cmds = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]
            for cmd in cmds:
                try:
                    output = subprocess.check_output([cmd, "--version"],
                    stderr=subprocess.STDOUT, text=True)
                    match = re.search(r"\d+\.\d+\.\d+\.\d+", output)
                    if match:
                        return match.group(0)
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue

        elif system == "Darwin":  # macOS
            output = subprocess.check_output(
                ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
                stderr=subprocess.STDOUT,
                text=True
            )
            match = re.search(r"\d+\.\d+\.\d+\.\d+", output)
            if match:
                return match.group(0)

    except (FileNotFoundError, subprocess.CalledProcessError, OSError) as e:
        logging.warning("не удалось определить версию Chrome: %s",e)
        return None

    return None


def setup_driver(headless: bool = True):
    """Создаёт и возвращает готовый WebDriver с учётом версии Chrome."""
    logging.getLogger("WDM").setLevel(logging.ERROR)

    chrome_version = get_chrome_version()
    if not chrome_version:
        raise RuntimeError("Не удалось определить версию Chrome.")

    print(f"🧭 Найдена версия Chrome: {chrome_version}")

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager(driver_version=chrome_version).install())
    drivercrome = webdriver.Chrome(service=service, options=options)
    print(F"✅ WebDriver версии {chrome_version} успешно создан.")
    return drivercrome
