# Generated by Django 3.1.1 on 2020-09-17 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0012_auto_20200917_1031'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Steps',
            new_name='Step',
        ),
    ]