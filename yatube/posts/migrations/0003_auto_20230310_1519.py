# Generated by Django 2.2.19 on 2023-03-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230306_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
