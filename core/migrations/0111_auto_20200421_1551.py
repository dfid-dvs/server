# Generated by Django 2.0.5 on 2020-04-21 10:06

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0110_auto_20200420_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gisstyle',
            name='field_color',
            field=colorfield.fields.ColorField(blank=True, default='#FF0000', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='gisstyle',
            name='style',
            field=colorfield.fields.ColorField(blank=True, default='#FF0000', max_length=18, null=True),
        ),
    ]
