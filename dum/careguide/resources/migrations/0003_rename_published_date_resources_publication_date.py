# Generated by Django 5.1.1 on 2024-09-15 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_alter_resources_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resources',
            old_name='published_date',
            new_name='publication_date',
        ),
    ]
