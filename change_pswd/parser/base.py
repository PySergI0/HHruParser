from abc import ABC, abstractmethod
from dataclasses import dataclass

from selenium.webdriver.remote.webelement import WebElement


@dataclass
class BaseParser(ABC):
    @abstractmethod
    def get(self, url: str):
        pass

    @abstractmethod
    def find_element_by_xpath(self, path: str):
        pass

    @abstractmethod
    def get_list_elements_by_xpath(self, path: str):
        pass

    @abstractmethod
    def get_attribute(self, path: str, attribute: str):
        pass

    @abstractmethod
    def click_element(self, path: str):
        pass

    @abstractmethod
    def send_keys(self, element: WebElement):
        pass


class BaseParserHH(ABC):    
    @abstractmethod
    def authorization(self):
        pass

    @abstractmethod
    def change_pwd(self):
        pass

    @abstractmethod
    def send_keys(self, value: str):
        pass
