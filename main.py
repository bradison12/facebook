# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import os
import time
import asyncio
from send_post import SendPost
from repost import RepostPost
from set_frends import SetFriends

mobile_emulation = {
    "deviceMetrics": {"width": 514, "height": 736, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1"
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=400,400")
chrome_options.headless = True
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
filename = 'cookies.pkl'
browser.get('https://www.facebook.com/')
if os.path.isfile(filename):
    print('ok')
    with open(filename, 'rb') as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        browser.add_cookie(cookie)
    time.sleep(1)
    browser.refresh()
else:
    time.sleep(5)
    search_box = browser.find_element(By.XPATH, '//input[@id="m_login_email"]')
    search_box.send_keys('+380632123515')
    del search_box
    search_box = browser.find_element(
        By.XPATH, '//input[@id="m_login_password"]')
    search_box.send_keys('Kolyan2010')
    del search_box
    search_box = browser.find_element(By.XPATH, '//*[@name="login"]')
    search_box.click()
    del search_box
while True:
    print(f"1: Send post in Facebook\n")
    print(f"2: Repost in Facebook\n")
    print(f"3: Get Friends Facebook\n")
    print(f"0: Exit\n")
    number = int(input('Який номер?'))
    if number == 1:
        rep = SendPost(browser=browser)
        asyncio.run(rep.send())
    elif number == 2:
        rep = RepostPost(browser=browser)
        asyncio.run(rep.start())
    elif number == 3:
        rep = SetFriends(browser=browser)
        asyncio.run(rep.send())
    elif number == 0:
        print(browser.get_cookies())
        with open(filename, 'wb') as file:
            pickle.dump(browser.get_cookies(), file)
        browser.quit()
        break
    # with open(filename, 'wb') as file:
    #     pickle.dump(browser.get_cookies(), file)
    # Закриваємо веб-браузер
