import time
from abc import ABC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
import web.utils.wait_utils as wait


class BasePage(ABC):
    def __init__(self, browser: WebDriver, url: str):
        self._browser = browser
        self._url = url

    def _click(self, locator, timeout=10, poll=0.5):
        self.wait_until_enabled(locator, "Элемент должен быть активен перед кликом", timeout, poll)
        self._browser.find_element(*locator).click()

    def _get_text(self, locator):
        self.wait_until_present(locator, "Элемент должен быть стабилен перед получением текста")
        return self._browser.find_element(*locator).text

    def _is_present(self, locator, get_element=False):
        try:
            el = self._browser.find_element(*locator)
            result = el if get_element else True
        except NoSuchElementException:
            result = False

        return result

    def _scroll_to(self, locator, shift_x=0, shift_y=0):
        el_location = self._browser.find_element(*locator).location
        x = el_location["x"] + shift_x
        y = el_location["y"] + shift_y
        self._browser.execute_script(
            "window.scrollTo({}, {})".format(x, y))
        self.wait_until_visible(locator, "Элемент должен быть видим после скролла на него")
        time.sleep(.5)

    def wait_until_visible(self, locator, message, timeout=10, poll=0.5):
        ec = EC.visibility_of_element_located(locator)
        wait.until_ec(self._browser, ec, "{}: {}".format(",".join(locator), message), timeout, poll=poll)

    def wait_until_enabled(self, locator, message, timeout=10, poll=0.5):
        ec = EC.element_to_be_clickable(locator)
        wait.until_ec(self._browser, ec, "{}: {}".format(",".join(locator), message), timeout=timeout, poll=poll)

    def wait_until_present(self, locator, message, timeout=10, poll=0.5):
        ec = EC.presence_of_element_located(locator)
        wait.until_ec(self._browser, ec, "{}: {}".format(",".join(locator), message), timeout=timeout, poll=poll)
