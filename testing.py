# test_api.py
import pytest
import requests

@pytest.fixture
def api_base():
    return 'http://127.0.0.1:8000/'
@pytest.fixture
def api_post():
    return 'http://127.0.0.1:8000/posts/'
@pytest.fixture
def api_images():
    return 'http://127.0.0.1:8000/images/'
@pytest.fixture
def api_tags():
    return 'http://127.0.0.1:8000/tags'

def test_get_posts(api_post):
    response = requests.get(api_post)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_images(api_images):
    response = requests.get(api_images)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

##TODO not passed
def test_get_tags(api_tags):
    response = requests.get(api_tags)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_create_user(api_url):
    new_user = {'username': 'johndoe', 'email': 'johndoe@example.com'}
    response = requests.post(api_url, json=new_user)
    assert response.status_code == 201
    assert response.json()['username'] == 'johndoe'
