# Generated by Django 3.1.1 on 2020-10-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201027_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
