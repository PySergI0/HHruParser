from dataclasses import dataclass
import random
from time import sleep
from typing import Optional

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


from parser.base import BaseParser, BaseParserHH
from parser.config import marks


@dataclass
class ParserHH(BaseParserHH):
    parser: Optional[WebDriver] = None

    def __post_init__(self) -> None:
        self.parser = uc.Chrome() if self.parser is None else self.parser

    def authorization(
        self,
        login: str,
        password: str,
        url: str = None
    ) -> None:

        if url is not None:
            self.parser.get(url)
        sleep(random.uniform(1, 3))

        input_login_elem = self.parser.find_element(
            By.XPATH, marks["login_xpath"])
        input_login_elem.send_keys(login)
        sleep(random.uniform(0.5, 3))
        del input_login_elem

        self.parser.find_element(
            By.XPATH, marks["login_by_password_text_btn"]).click()
        sleep(random.uniform(0.5, 3))

        input_password_elem = self.parser.find_element(
            By.XPATH, marks["password"])
        input_password_elem.send_keys(password)
        sleep(random.uniform(0.5, 2))
        input_password_elem.send_keys(Keys.ENTER)
        del input_password_elem

        sleep(random.uniform(1, 5))

        solve_captcha(chrome_driver)
