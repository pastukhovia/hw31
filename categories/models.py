from django.core.exceptions import ValidationError
from django.db import models


def slug_length_validation(value: str):
    if len(value) < 5:
        raise ValidationError('Ensure this field has no more than 5 characters.')


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, validators=[slug_length_validation], max_length=10)

    def __str__(self):
        return self.name
