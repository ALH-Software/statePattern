# Generated by Django 2.0.5 on 2020-04-21 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_auto_20200422_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='next',
            field=models.IntegerField(default=-1),
        ),
    ]
