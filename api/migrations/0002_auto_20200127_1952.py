# Generated by Django 3.0.2 on 2020-01-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='picture',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
