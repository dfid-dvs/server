# Generated by Django 2.0.5 on 2019-11-13 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_remove_project_partner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='program',
            new_name='program_id',
        ),
    ]