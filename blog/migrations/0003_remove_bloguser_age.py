# Generated by Django 2.2.6 on 2021-08-31 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210831_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='age',
        ),
    ]
