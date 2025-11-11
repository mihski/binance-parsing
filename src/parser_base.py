from chrome import get_chrome_driver


class Base_Parser:
    """
    базовый клас для парсинга страниц с таблицаим
    """
    def __init__(self,url: str):

        self.url=url
        self.driver = get_chrome_driver()

    def open_page(self):
        self.driver.get(self.url)


    def fetch_tanle():
        pass

    def close(self):
        """Закрывает браузер."""
        if self.driver:
            self.driver.quit()


