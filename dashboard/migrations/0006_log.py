# Generated by Django 2.0.5 on 2019-11-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
