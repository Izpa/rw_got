# Generated by Django 2.2.1 on 2019-05-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_auto_20190503_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='all_members_are_administrators',
            field=models.NullBooleanField(),
        ),
    ]
