# Generated by Django 2.0.5 on 2019-09-25 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20190925_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='sector_name',
            new_name='name',
        ),
    ]