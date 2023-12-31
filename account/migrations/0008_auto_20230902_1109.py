# Generated by Django 3.2.20 on 2023-09-02 11:09

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20230902_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teenuserprofile',
            name='date_of_birth',
            field=models.DateField(help_text='Enter date as: mm/dd/yyyy', null=True),
        ),
        migrations.AlterField(
            model_name='teenuserprofile',
            name='medical_id',
            field=models.CharField(help_text='Required: 7 digit number on your wristband', max_length=7, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(7)]),
        ),
    ]
