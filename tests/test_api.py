import allure
import pytest




@allure.feature('API tests')
@pytest.mark.api
def test_list_users(api_client):
"""1. GET /users?page=2 вернёт статус 200 и список пользователей"""
r = api_client.get('/users', params={'page': 2})
assert r.status_code == 200
data = r.json()
assert 'data' in data and isinstance(data['data'], list)




@pytest.mark.api
def test_get_single_user(api_client):
"""2. GET /users/2 вернёт существующего пользователя"""
r = api_client.get('/users/2')
assert r.status_code == 200
data = r.json()
assert data.get('data', {}).get('id') == 2




@pytest.mark.api
def test_create_user(api_client):
"""3. POST /users создаёт пользователя и возвращает 201"""
payload = {'name': 'autotest', 'job': 'tester'}
r = api_client.post('/users', json=payload)
assert r.status_code == 201
data = r.json()
assert data['name'] == payload['name']
assert 'id' in data




@pytest.mark.api
def test_update_user(api_client):
"""4. PUT /users/2 обновляет и возвращает 200"""
payload = {'name': 'autotest_updated', 'job': 'senior tester'}
r = api_client.put('/users/2', json=payload)
assert r.status_code == 200
data = r.json()
assert data['name'] == payload['name']




@pytest.mark.api
def test_delete_user(api_client):
"""5. DELETE /users/2 возвращает 204"""
r = api_client.delete('/users/2')
assert r.status_code == 204
