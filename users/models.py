from datetime import date, timedelta

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from locations.models import Location


def check_age(value: date):
    if date.today() - value < timedelta(days=(365 * 9)):
        raise ValidationError('User should be older than 9 years.')


def check_email_if_rambler(value: str):
    if value.endswith('rambler.ru'):
        raise ValidationError('You cannot use Rambler email.')


class User(AbstractUser):
    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    MEMBER = 'member'
    ROLES = [
        (ADMIN, ADMIN),
        (MODERATOR, MODERATOR),
        (MEMBER, MEMBER)
    ]

    role = models.CharField(max_length=9, choices=ROLES, default=MEMBER)
    age = models.IntegerField(default=0, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(validators=[check_age])
    email = models.EmailField(unique=True, validators=[check_email_if_rambler])

    def __str__(self):
        return self.username
