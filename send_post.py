
import time
from functions import AIsearcher
from selenium.webdriver.common.by import By


class SendPost:
    def __init__(self, browser):
        self.browser = browser
        self.ai = AIsearcher()

    async def send(self):
        search_box = self.browser.find_element(
            By.XPATH, '//*[@role="button"][@tabindex="0"]')
        search_box.click()
        del search_box
        time.sleep(2)

        await self.ai.get_prompt_response_text()
        search_box = self.browser.find_element(By.XPATH, '//*[@id="uniqid_1"]')
        search_box.send_keys(f"{self.ai.response['choices'][0]['text']}")
        del search_box
        time.sleep(2)

        search_box = self.browser.find_element(
            By.XPATH, '//*[@id="composer-main-view-id"]/div[3]/div/div/button')
        search_box.click()
        del search_box
