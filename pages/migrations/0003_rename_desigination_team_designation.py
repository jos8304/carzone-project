# Generated by Django 4.2.10 on 2024-11-05 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desigination',
            new_name='designation',
        ),
    ]
