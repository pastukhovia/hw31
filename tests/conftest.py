import pytest

from pytest_factoryboy import register

from factories import UserFactory, AdFactory

register(UserFactory)
register(AdFactory)


@pytest.fixture
@pytest.mark.django_db
def login(django_user_model, client):
    username = 'test'
    password = 'test'
    birth_date = '2000-01-01'
    role = 'member'

    user = django_user_model.objects.create_user(username=username,
                                                 password=password,
                                                 birth_date=birth_date,
                                                 role=role)

    response = client.post('/user/token/',
                           {
                               "username": username,
                               "password": password
                           },
                           format='json')

    return response.data['access'], user.pk
