from selenium.webdriver.common.by import By
from .base_page import BasePage




class LoginPage(BasePage):
USERNAME = (By.ID, 'username')
PASSWORD = (By.ID, 'password')
LOGIN_BTN = (By.CSS_SELECTOR, 'button.radius')
FLASH = (By.ID, 'flash')


def open_login(self):
self.open('/login')


def login(self, username: str, password: str):
self.wait_visible(self.USERNAME).clear()
self.wait_visible(self.USERNAME).send_keys(username)
self.wait_visible(self.PASSWORD).clear()
self.wait_visible(self.PASSWORD).send_keys(password)
self.wait_clickable(self.LOGIN_BTN).click()


def get_flash_text(self) -> str:
return self.wait_visible(self.FLASH).text
