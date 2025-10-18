Проект по автоматизации тестирования (UI + API)

📘 Описание проекта

Данный проект — реальное решение по автоматизации тестирования, включающее:

UI-тесты для сайта The Internet

API-тесты для сервиса ReqRes

Проект выполнен в рамках финального задания курса по автоматизации тестирования. Цель — автоматизировать ключевые сценарии из ручного тестирования и оформить стабильный, переиспользуемый фреймворк.

⚙️ Структура проекта

autotests_project/
├── tests/
│   ├── test_ui.py          # UI-тесты (Selenium)
│   ├── test_api.py         # API-тесты (Requests)
│   ├── conftest.py         # Фикстуры, инициализация драйвера
│
├── pages/                  # Page Object классы для UI-тестов
│   ├── base_page.py
│   ├── login_page.py
│   ├── secure_page.py
│
├── data/
│   ├── test_data.py        # Тестовые данные и учётные записи
│   ├── config.py           # Настройки окружения (URL и пути)
│
├── requirements.txt        # Зависимости проекта
├── README.md               # Этот файл
├── .env.example            # Пример переменных окружения
└── pytest.ini              # Маркеры pytest

🔧 Установка и запуск

1. Клонируйте репозиторий

git clone https://github.com/<your_username>/real_autotests_project.git
cd real_autotests_project

2. Создайте виртуальное окружение и установите зависимости

python -m venv venv
source venv/bin/activate  # для Linux / Mac
venv\Scripts\activate     # для Windows
pip install -r requirements.txt

3. Настройте окружение

Создайте файл .env, скопировав .env.example, и укажите нужные параметры (например, BASE_URL, LOGIN, PASSWORD).

🚀 Запуск тестов

Запуск всех тестов

pytest --alluredir=allure-results

Только UI-тесты

pytest -m ui --alluredir=allure-results

Только API-тесты

pytest -m api --alluredir=allure-results

Генерация отчета Allure

allure serve allure-results

🧩 Используемые технологии

Python 3.11+

Selenium WebDriver — автоматизация UI

Requests — автоматизация API

Pytest — фреймворк тестирования

Allure — отчётность

dotenv — работа с переменными окружения

flake8 — проверка стиля кода

🧠 Примеры тестов

UI-тест (Login)

@allure.title('Успешный вход в систему')
@allure.feature('UI')
@pytest.mark.ui
def test_success_login(driver, login_page):
    login_page.open()
    login_page.login('tomsmith', 'SuperSecretPassword!')
    assert login_page.get_success_message() == 'You logged into a secure area!'

API-тест (Создание пользователя)

@allure.title('Создание нового пользователя')
@allure.feature('API')
@pytest.mark.api
def test_create_user():
    response = requests.post('https://reqres.in/api/users', json={'name': 'Tsyren', 'job': 'tester'})
    assert response.status_code == 201
    assert response.json()['name'] == 'Tsyren'

🧾 Лицензия и автор

Автор: Tsyren Dorzhizhapovich GomboevГод: 2025Курс: «Автоматизация тестирования»Контакт: GitHub Profile
