# Generated by Django 5.0.3 on 2024-05-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0004_food_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='UserID',
            field=models.CharField(max_length=40),
        ),
    ]