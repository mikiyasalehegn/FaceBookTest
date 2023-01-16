from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class BasePage:
    _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def _find(self, by, locate) -> WebElement:
        return self._driver.find_element(by, locate)

    def _entry(self, by, locate, content):
        self._wait_until_element_is_visible(by, locate)
        self._find(by, locate).send_keys(content)

    def _wait_until_element_is_visible(self, by, locate, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located((by, locate)))

    def _click(self, by, locate):
        self._wait_until_element_is_visible(by, locate)
        self._find(by, locate).click()

    def _is_displayed(self, by, locate) -> bool:
        try:
            return self._find(by, locate).is_displayed()
        except NoSuchElementException:
            return False

    def _message(self, by, locate):
        self._wait_until_element_is_visible(by, locate)
        return self._find(by, locate).text

    def _clear(self, by, locate):
        self._wait_until_element_is_visible(by, locate)
        self._find(by, locate).clear()

    def _select(self, by, locate, year: str = "2000"):
        birth = Select(self._find(by, locate))
        birth.select_by_value(year)