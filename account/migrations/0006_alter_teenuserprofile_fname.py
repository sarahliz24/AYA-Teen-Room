# Generated by Django 3.2.20 on 2023-09-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_teenuserprofile_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teenuserprofile',
            name='fname',
            field=models.CharField(blank=True, help_text='Optional', max_length=20, null=True, verbose_name='first name'),
        ),
    ]
