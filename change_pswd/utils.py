import random
from datetime import datetime
import secrets
import string
import pytesseract
from io import BytesIO
from PIL import Image

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from parser.config import marks, months


def solve_captcha(driver: webdriver):
    try:
        captcha_element = driver.find_element(
            By.CLASS_NAME, marks["captcha_class"])
    except NoSuchElementException:
        print("капчи нет")
        return
    else:
        captcha_img = captcha_element.screenshot_as_png
        image = Image.open(BytesIO(captcha_img))
        captcha_text = pytesseract.image_to_string(
            image, config='--psm 8 --oem 3')
        print("CAPTCHA Text:", captcha_text)
        return captcha_text


def generate_pwd(pwd_length: int) -> str:
    lower_letters = string.ascii_lowercase
    upper_letter = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    new_pwd = ""
    for i in range(0, 2):
        new_pwd += "".join(secrets.choice(lower_letters))
        new_pwd += "".join(secrets.choice(upper_letter))
        new_pwd += "".join(secrets.choice(digits))
        new_pwd += "".join(secrets.choice(special_chars))

    alphabet = lower_letters + upper_letter + digits + special_chars

    for i in range(pwd_length-4):
        new_pwd += "".join(secrets.choice(alphabet))
    print(new_pwd)
    char_list = list(new_pwd)
    random.shuffle(char_list)
    shuffled_pwd = "".join(char_list)
    return shuffled_pwd

# print(generate_pwd(8))


def transformation_to_date(period: str) -> str:
    list_str = period.split()
    month = list_str.pop()
    number_month = months[month]
    number = list_str.pop()

    now = datetime.now()
    current_year = datetime.today().year
    date = datetime(int(current_year), int(number_month), int(number))
    if date > now:
        return date
    else:
        return datetime(int(current_year) + 1, int(number_month), int(number))


print(transformation_to_date("Действует до 12 января"))
