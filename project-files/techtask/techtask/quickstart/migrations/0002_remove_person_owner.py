# Generated by Django 4.0.6 on 2022-07-26 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='owner',
        ),
    ]
