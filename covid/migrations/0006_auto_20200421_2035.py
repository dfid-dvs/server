# Generated by Django 2.0.5 on 2020-04-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0005_auto_20200421_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='drydeshospuncoveredadm1sums',
            name='gn_type',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='drydeshospuncoveredadm1sums',
            name='gn_type_1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='drydeshospuncoveredadm1sums',
            name='palika',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
