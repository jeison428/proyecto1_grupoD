# Generated by Django 2.2.3 on 2020-10-29 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('d_information_management_app', '0002_professor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicTraining',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('institucion', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='d_information_management_app.Professor')),
            ],
            options={
                'verbose_name': 'FormacionAcademica',
                'verbose_name_plural': 'FormacionesAcademicas',
            },
        ),
    ]