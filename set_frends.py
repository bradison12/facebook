
import time
from selenium.webdriver.common.by import By


class SetFriends:
    def __init__(self, browser):
        self.browser = browser

    async def send(self):
        search_box = self.browser.find_element(
            By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/a')
        search_box.click()
        del search_box
        time.sleep(2)
        search_box = self.browser.find_elements(By.XPATH, '//button[@type="submit"]')
        inter = 0
        for button in search_box:
            if inter == 20:
                self.browser.refresh()
                time.sleep(86400)
            time.sleep(2)
            button.click()
            inter += 1