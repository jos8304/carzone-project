# Generated by Django 4.2.10 on 2024-11-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
