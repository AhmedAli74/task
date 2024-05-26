# Generated by Django 5.0.4 on 2024-05-02 11:40

import exams.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=exams.models.Upload)),
                ('faculaty', models.CharField(max_length=200)),
                ('count_of_subjects', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]