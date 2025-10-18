import os
import pytest
from dotenv import load_dotenv
from utils.api_client import ApiClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


load_dotenv()


BASE_URL = os.getenv('BASE_URL', 'https://the-internet.herokuapp.com')
API_BASE = os.getenv('API_BASE_URL', 'https://reqres.in/api')
HEADLESS = os.getenv('HEADLESS', 'true').lower() in ('1', 'true', 'yes')




@pytest.fixture(scope='session')
def base_url():
return BASE_URL




@pytest.fixture(scope='session')
def api_base_url():
return API_BASE




@pytest.fixture(scope='session')
def api_client():
return ApiClient(base_url=API_BASE)




@pytest.fixture
def driver():
options = webdriver.ChromeOptions()
if HEADLESS:
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
yield driver
driver.quit()
