# Generated by Django 5.0.3 on 2024-04-12 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_tercera', '0005_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.IntegerField()),
            ],
        ),
    ]