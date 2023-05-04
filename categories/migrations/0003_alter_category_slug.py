# Generated by Django 4.2 on 2023-05-04 14:36

import categories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, unique=True, validators=[categories.models.slug_length_validation]),
        ),
    ]