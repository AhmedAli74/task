# Generated by Django 5.0.4 on 2024-05-09 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_subject_is_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='slug',
            new_name='slugy',
        ),
    ]