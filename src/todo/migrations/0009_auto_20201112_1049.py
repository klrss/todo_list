# Generated by Django 3.1.1 on 2020-11-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20201111_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
