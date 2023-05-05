import factory

from ads.models import Ad
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'test'
    password = 'test'
    birth_date = '2000-01-01'
    role = 'member'


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test name for ad"
    is_published = False
    price = 10
