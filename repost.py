import time
from selenium.webdriver.common.by import By


class RepostPost:
    def __init__(self, browser):
        self.browser = browser

    async def start(self):
        i = 0
        while True:
            if i == 20:
                break
            search_box = self.browser.find_element(
                By.XPATH, '//*[@data-sigil="share-popup"]')
            search_box.click()
            searchone = self.browser.find_element(
                By.XPATH, '//*[@data-sigil="touchable touchable share-one-click-button"]')
            searchone.click()
            time.sleep(60)
            self.browser.refresh()
            time.sleep(2)
            del searchone
            del search_box
            print(f"Було зарепостчено: $ - {i}")
            i += 1
