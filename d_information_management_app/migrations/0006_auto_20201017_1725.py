# Generated by Django 2.2.3 on 2020-10-17 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('d_information_management_app', '0005_auto_20201017_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupoinvestigacion',
            name='id_institucion',
        ),
        migrations.AddField(
            model_name='grupoinvestigacion',
            name='institucion',
            field=models.ForeignKey(default=11111, on_delete=django.db.models.deletion.CASCADE, to='d_information_management_app.Institucion'),
            preserve_default=False,
        ),
    ]
