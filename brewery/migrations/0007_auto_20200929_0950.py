# Generated by Django 3.1.1 on 2020-09-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery', '0006_auto_20200929_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]