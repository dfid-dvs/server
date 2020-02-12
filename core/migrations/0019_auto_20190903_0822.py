# Generated by Django 2.0.4 on 2019-09-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_indicator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gapanapa',
            old_name='code',
            new_name='cbs_code',
        ),
        migrations.RenameField(
            model_name='gapanapa',
            old_name='gapaNapa_name',
            new_name='gn_type',
        ),
        migrations.AddField(
            model_name='gapanapa',
            name='hlcit_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gapanapa',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gapanapa',
            name='p_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]