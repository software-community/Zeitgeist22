# Generated by Django 4.0 on 2021-12-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='college',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='participation',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='user',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
