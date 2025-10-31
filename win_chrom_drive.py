import winreg

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
