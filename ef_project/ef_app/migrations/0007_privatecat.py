# Generated by Django 5.1.6 on 2025-03-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ef_app', '0006_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Приватная категория',
                'verbose_name_plural': 'Приватные категории',
            },
        ),
    ]
