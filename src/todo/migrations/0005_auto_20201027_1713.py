# Generated by Django 3.1.1 on 2020-10-27 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20201027_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='todo.projects'),
        ),
    ]
