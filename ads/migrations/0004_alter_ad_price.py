# Generated by Django 4.2 on 2023-05-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.IntegerField(),
        ),
    ]
