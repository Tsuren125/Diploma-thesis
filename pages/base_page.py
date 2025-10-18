from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class BasePage:
def __init__(self, driver, base_url: str):
self.driver = driver
self.base_url = base_url


def open(self, path: str = "") -> None:
url = self.base_url.rstrip('/') + '/' + path.lstrip('/')
self.driver.get(url)


def wait_visible(self, locator, timeout=10):
return WebDriverWait(self.driver, timeout).until(
EC.visibility_of_element_located(locator)
)


def wait_clickable(self, locator, timeout=10):
return WebDriverWait(self.driver, timeout).until(
EC.element_to_be_clickable(locator)
)
