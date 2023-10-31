class_text = """import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser():
    def __init__(self, driver_path,headless = True) -> None:
        self.options = webdriver.FirefoxOptions()
        if not headless:
            self.options.add_argument("--headless")  # Включаем безголов
        try:    
            self.service = webdriver.FirefoxService(executable_path=driver_path)
        except:
            print("Нет драйвера firefox")
            return
        self.driver = webdriver.Firefox(service = self.service, options = self.options)

    def quit(self):
        #Закрываем все
        self.driver.quit()

    def close_window(self):
        #Закрываем окно
        self.driver.close()

    def visite_main_page(self, url, sec_sleep = 1)->None:
        #Открывает основную страницу
        try:
            self.driver.get(url)
            time.sleep(sec_sleep)
        except:
            print("Страница не найдена")

    def get_links_in_div(self, el):
        #получает все ссылки из элемента
        try:
            link_tag = el.find_element(By.TAG_NAME, "a")
            return link_tag.get_attribute("href")
        except:
            print(f"В элементе {el.tag_name} нет ссылок с тегом <a>.")
"""