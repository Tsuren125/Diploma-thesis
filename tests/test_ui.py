import pytest
page.login('tomsmith', 'SuperSecretPassword!')
text = page.get_flash_text()
assert 'You logged into a secure area!' in text




@pytest.mark.ui
def test_form_auth_failure(driver, base_url):
"""2. Неправильная авторизация показывает ошибку"""
page = LoginPage(driver, base_url)
page.open_login()
page.login('wrong', 'credentials')
text = page.get_flash_text()
assert 'Your username is invalid!' in text or 'Your password is invalid!' in text




@pytest.mark.ui
def test_add_remove_elements(driver, base_url):
"""3. Добавление и удаление элементов на странице /add_remove_elements/"""
driver.get(base_url + '/add_remove_elements/')
add_btn = driver.find_element(By.XPATH, "//button[text()='Add Element']")
add_btn.click()
# после клика появляется кнопка Delete
delete_btn = driver.find_element(By.CLASS_NAME, 'added-manually')
assert delete_btn.is_displayed()
delete_btn.click()
# после удаления нет кнопки
elems = driver.find_elements(By.CLASS_NAME, 'added-manually')
assert len(elems) == 0




@pytest.mark.ui
def test_checkbox_toggle(driver, base_url):
"""4. Чекбоксы на /checkboxes можно переключать"""
driver.get(base_url + '/checkboxes')
boxes = driver.find_elements(By.CSS_SELECTOR, '#checkboxes input[type=checkbox]')
assert len(boxes) >= 2
# переключаем первый
boxes[0].click()
assert boxes[0].is_selected() is True




@pytest.mark.ui
def test_dynamic_loading(driver, base_url):
"""5. Пример динамической загрузки /dynamic_loading/1"""
driver.get(base_url + '/dynamic_loading/1')
start = driver.find_element(By.TAG_NAME, 'button')
start.click()
# ждём пока появится элемент Hello World
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'finish')))
finish = driver.find_element(By.ID, 'finish')
assert 'Hello World' in finish.text
