# Generated by Django 4.2.10 on 2024-11-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
    ]
