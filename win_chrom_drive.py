import winreg
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_version() -> str:
    """
    Определяет версию Chrome через реестр Windows.
    """
    try:
        # Сначала смотрим текущего пользователя
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Google\Chrome\BLBeacon")
        version, _ = winreg.QueryValueEx(key, "version")
        return version
    except FileNotFoundError:
        try:
            # Потом локальная машина
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r"Software\Google\Chrome\BLBeacon")
            version, _ = winreg.QueryValueEx(key, "version")
            return version
        except FileNotFoundError:
            return None

chrome_ver = get_chrome_version()
print("Версия Chrome из реестра:", chrome_ver)

def setup_driver(headless: bool = False):
    """Создаёт и возвращает готовый WebDriver с учётом версии Chrome."""
    logging.getLogger("WDM").setLevel(logging.ERROR)

    chrome_version = get_chrome_version()
    if not chrome_version:
        raise RuntimeError("Не удалось определить версию Chrome.")

    print(f"🧭 Найдена версия Chrome: {chrome_version}")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager(driver_version=chrome_version).install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

if __name__ == "__main__":
    driver = setup_driver(headless=False)

    driver.get("https://www.google.com")
    print("🌍 Страница:", driver.title)
    driver.quit()
