# Generated by Django 5.0.3 on 2024-05-28 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_authentication_user_parametres'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='UserID',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='counter.authentication'),
            preserve_default=False,
        ),
    ]
