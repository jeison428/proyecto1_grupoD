# Generated by Django 2.2.3 on 2020-10-19 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_information_management_app', '0008_auto_20201018_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='es_interno',
            field=models.BooleanField(default=False),
        ),
    ]