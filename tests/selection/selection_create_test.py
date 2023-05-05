import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, login):
    ads = AdFactory.create_batch(4)
    access_token, user_id = login

    expected_data = {
        "id": 1,
        "items": [
            ad.pk for ad in ads
        ],
        "name": "test",
        "owner": user_id
    }

    data = {
        "name": "test",
        "items": [ad.pk for ad in ads]
    }

    response = client.post('/selection/create/', data, format='json', HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 201
    assert response.data == expected_data


@pytest.mark.django_db
def test_selection_unauthorized(client):
    ads = AdFactory.create_batch(4)

    data = {
        "name": "test",
        "items": [ad.pk for ad in ads]
    }

    response = client.post('/selection/create/', data, format='json')

    assert response.status_code == 401
    assert response.content == b'{"detail":"Authentication credentials were not provided."}'
