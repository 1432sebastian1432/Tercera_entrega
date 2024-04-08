# Generated by Django 5.0.3 on 2024-04-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_tercera', '0003_remove_curso_camada_alter_curso_nombre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.AddField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
