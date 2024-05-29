# Generated by Django 5.0.3 on 2024-05-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('FoodID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Calories', models.FloatField()),
                ('Datetime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]