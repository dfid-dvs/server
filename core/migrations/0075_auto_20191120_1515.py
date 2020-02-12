# Generated by Django 2.0.5 on 2019-11-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='female_achieved_2011_2015',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='female_achieved_2011_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='female_achieved_2015_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='female_forecast_2011_2015',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='female_forecast_2011_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='female_forecast_2015_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='male_achieved_2011_2015',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='male_achieved_2011_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='male_achieved_2015_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='male_forecast_2011_2015',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='male_forecast_2011_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='male_forecast_2015_2019',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]