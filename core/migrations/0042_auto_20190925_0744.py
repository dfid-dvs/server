# Generated by Django 2.0.5 on 2019-09-25 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20190925_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsector',
            old_name='sub_sector_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='subsector',
            old_name='sub_sector_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subsector',
            old_name='sector',
            new_name='sector_id',
        ),
    ]
