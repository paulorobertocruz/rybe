# Generated by Django 3.1.5 on 2021-01-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('codigo', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
    ]
