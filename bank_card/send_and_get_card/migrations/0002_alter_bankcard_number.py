# Generated by Django 4.2.3 on 2023-07-10 00:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('send_and_get_card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcard',
            name='number',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
