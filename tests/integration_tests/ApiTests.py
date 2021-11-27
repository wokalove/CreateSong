import requests

def test_get_users_status(self):
    expected_result = { "user1": "active",  "user2": "inactive" }
    r = requests.get('https://localhost:8080/get_users_status', auth=('user', 'pass'))
    assert r.status_code is 200
    self.write_json(expected_result, r.json())

# https://stackoverflow.com/questions/55470731/integration-test-in-python
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/testing.html