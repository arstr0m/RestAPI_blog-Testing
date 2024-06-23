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


##GET ALL FIELDS
def test_get_fields_posts():
    response = requests.get('http://127.0.0.1:8000/posts/')
    assert response.status_code == 200
    data = response.json()
    assert 'title' in data
    assert isinstance(data['title'], str)
    assert len(data['title']) > 0
    assert 'body' in data
    assert isinstance(data['body'], str)
    assert len(data['body']) > 0
    assert 'status' in data
    assert isinstance(data['status'], str)
    assert len(data['status']) > 0 and len(data['status']) <= 3
    assert 'has_image' in data
    assert isinstance(data['has_image'], bool)
    assert 'publishing_date' in data
    assert isinstance(data['publishing_date'], str)

# Get all fields
def test_get_all_fields_images():
    response = requests.get('http://127.0.0.1:8000/images/')
    assert response.status_code == 200
    data = response.json()
    assert 'url' in data
    assert 'caption' in data
    assert isinstance(data['url'], str)
    assert isinstance(data['caption'], str)
    assert len(data['caption']) <= 50 and len(data['caption']) > 0
    assert len(data['url']) <= 245 and len(data['url']) > 0

# get all tags
def test_get_all_fields_tags():
    response = requests.get('http://127.0.0.1:8000/tags/all')
    assert response.status_code == 200
    data = response.json()
    assert 'title' in data
    assert 'status' in data
    assert isinstance(data['status'], str)
    assert len(data['status']) > 0 and len(data['status']) <= 3
    assert isinstance(data['title'], str)
    assert len(data['title']) > 0


# GET RANDOM
def test_get_posts(api_post):
    response = requests.get(api_post)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_images(api_images):
    response = requests.get(api_images)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


# TODO not passed
def test_get_tags(api_tags):
    response = requests.get(api_tags)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# GET BY ID -> using 2,6 IT SAYS {
#     "detail": "Internal Server Error 400: The id: 2 you requested for does not exist"
# }
def test_get_post_by_id():
    id = 5
    response = requests.get(f"http://127.0.0.1:8000/posts/{id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    data = response.json()
    assert 'title' in data
    assert isinstance(data['title'], str)
    assert len(data['title']) > 0
    assert 'body' in data
    assert isinstance(data['body'], str)
    assert len(data['body']) > 0
    assert 'status' in data
    assert isinstance(data['status'], str)
    assert len(data['status']) > 0 and len(data['status']) <= 3
    assert 'has_image' in data
    assert isinstance(data['has_image'], bool)
    assert 'publishing_date' in data
    assert isinstance(data['publishing_date'], str)
#TODO NOT WORKING
def test_get_all_fields_images_by_id():
    id = 4
    response = requests.get(f'http://127.0.0.1:8000/images/{id}')
    assert response.status_code == 200
    data = response.json()
    assert 'url' in data
    assert 'caption' in data
    assert isinstance(data['url'], str)
    assert isinstance(data['caption'], str)
    assert len(data['caption']) <= 50 and len(data['caption']) > 0
    assert len(data['url']) <= 245 and len(data['url']) > 0
# GET ALL
def test_get_all_tags():
    response = requests.get('http://127.0.0.1:8000/tags/all')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_all_images():
    response = requests.get('http://127.0.0.1:8000/images/all')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_all_posts():
    response = requests.get('http://127.0.0.1:8000/posts/all')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# POST
def test_create_post():
    new_post = {
        'title': 'My New Post',
        'body': 'This is the content of my new post.',
        'has_image': False,
        'publishing_date': '2024-06-22T19:43:55.567000-06:00',
        'status': 'ACT'
    }
    response = requests.post('http://127.0.0.1:8000/posts/', json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, dict)
    assert data['title'] == new_post['title']
    assert data['body'] == new_post['body']
    assert data['has_image'] == new_post['has_image']
    assert data['publishing_date'] == new_post['publishing_date']
    assert data['status'] == new_post['status']

#TODO checkear  where False = isinstance([{'caption': 'picture taken from google', 'url': 'https://google.com'}], map)
def test_create_image():
    new_image = {
        "url": "https://google.com",
        "caption": "picture taken from google"
    }
    response = requests.post('http://127.0.0.1:8000/images/', json=new_image)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, map)
    assert 'url' in data
    assert 'caption' in data
    assert data['url'] == new_image['url']
    assert data['caption'] == new_image['caption']

#TODO chequear   where False = isinstance([{'status': 'ACT', 'title': 'Viajes'}], map)
def test_create_tag():
    new_tag = {
        "title": "Viajes",
        "status": "ACT"
    }
    response = requests.post('http://127.0.0.1:8000/tags/', json=new_tag)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, map)
    assert 'title' in data
    assert 'status' in data
    assert data['title'] == new_tag['title']
    assert data['status'] == new_tag['status']