# Generated by Django 2.0.4 on 2019-09-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20190906_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gapanapa',
            old_name='gn_type',
            new_name='gn_type_en',
        ),
        migrations.AddField(
            model_name='gapanapa',
            name='gn_type_np',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]