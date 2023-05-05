import pytest


@pytest.mark.django_db
def test_ad_create(client, user):
    excepted_response = {
        "id": 1,
        "desc": None,
        "is_published": False,
        "name": "test title for ad",
        "price": 123,
        "image": None,
        "author": 1,
        "category": None
    }

    data = {
        "name": "test title for ad",
        "is_published": False,
        "price": 123,
        "author": user.pk
    }

    response = client.post('/ad/create/', data, content_type='application/json')

    assert response.status_code == 201
    assert response.data == excepted_response


@pytest.mark.django_db
def test_is_published(client, user):
    data = {
        "name": "test title for ad",
        "is_published": True,
        "price": 123,
        "author": user.pk
    }

    response = client.post('/ad/create/', data, content_type='application/json')

    assert response.content == b'{"is_published":["This field cannot be True"]}'
    assert response.status_code == 400


@pytest.mark.django_db
def test_name_less_than_ten_char(client, user):
    data = {
        "name": "test",
        "is_published": False,
        "price": 123,
        "author": user.pk
    }

    response = client.post('/ad/create/', data, content_type='application/json')

    assert response.content == b'{"name":["Name of ad cannot be less than 10 characters."]}'
    assert response.status_code == 400


@pytest.mark.django_db
def test_name_blank(client, user):
    data = {
        "name": "",
        "is_published": False,
        "price": 123,
        "author": user.pk
    }

    response = client.post('/ad/create/', data, content_type='application/json')

    assert response.content == b'{"name":["This field may not be blank."]}'
    assert response.status_code == 400


@pytest.mark.django_db
def test_price(client, user):
    data = {
        "name": "test name for ad",
        "is_published": False,
        "price": -10,
        "author": user.pk
    }

    response = client.post('/ad/create/', data, content_type='application/json')

    assert response.content == b'{"price":["Ensure this value is greater than or equal to 0."]}'
    assert response.status_code == 400
