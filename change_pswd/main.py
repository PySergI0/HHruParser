import random
from time import sleep

import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from parser.config import marks
from utils import generate_pwd, solve_captcha


url = "https://nizhny-tagil.hh.ru/employer/settings"

login = "astrakhan-nl@sms19.ru"
password = "jma-MCr-wXL-kL211"
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

chrome_driver = webdriver.Chrome(options=chrome_options)


def authorization():
    chrome_driver.get(url)
    sleep(random.uniform(1, 3))
    input_login_elem = chrome_driver.find_element(By.XPATH, marks["login"])

    input_login_elem.send_keys(login)
    sleep(random.uniform(1, 5))

    chrome_driver.find_element(
        By.XPATH, marks["login_by_password_text_btn"]).click()
    sleep(random.uniform(1, 3))
    input_password_elem = chrome_driver.find_element(
        By.XPATH, marks["password"])
    input_password_elem.send_keys(password)
    sleep(random.uniform(1, 2))
    input_password_elem.send_keys(Keys.ENTER)
    sleep(random.uniform(1, 5))
    solve_captcha(chrome_driver)


authorization()

validity_period = chrome_driver.find_element(
    By.XPATH, marks["validity_period_pwd"])
print(validity_period.text.split()[-2:])


def change_pwd():
    chrome_driver.find_element(By.XPATH, marks["change_password_btn"]).click()
    new_password = generate_pwd()
    sleep(random.uniform(1, 5))
    old_password_element = chrome_driver.find_element(
        By.ID, marks["old_pasword_id"])
    old_password_element.send_keys(password)
    sleep(random.uniform(1, 3))
    new_password_element = chrome_driver.find_element(
        By.ID, marks["new_pasword_id"])
    new_password_element.send_keys(new_password)
    sleep(random.uniform(1, 3))
    new_password_confirm = chrome_driver.find_element(
        By.ID, marks["new_pasword_confirm_id"])
    new_password_confirm.send_keys(new_password)
    sleep(random.uniform(1, 3))
    new_password_confirm.send_keys(Keys.ENTER)

# change_pwd()


sleep(50)
chrome_driver.quit()
