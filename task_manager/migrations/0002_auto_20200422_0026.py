# Generated by Django 2.0.5 on 2020-04-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.SmallIntegerField(choices=[(0, 'New'), (1, 'In Progress'), (2, 'Done')], default=0),
        ),
    ]
