# Generated by Django 4.0 on 2021-12-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registration_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
