# Generated by Django 2.0.5 on 2019-11-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_auto_20191113_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='fivew',
            name='ward',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]