# Generated by Django 4.0 on 2021-12-16 10:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeName', models.CharField(max_length=200, verbose_name='College Name')),
                ('campusAmbassadorCode', models.CharField(max_length=15, unique=True, verbose_name='CA Code')),
                ('mobileNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN', verbose_name='Mobile Number')),
                ('whyInterested', models.TextField(verbose_name='Why do you want to be a Campus Ambassador?')),
                ('pastExperience', models.TextField(verbose_name='Do you have any past experience related to this? If yes, then please share your experience')),
            ],
            options={
                'verbose_name_plural': 'Registration details',
            },
        ),
    ]
