# Generated by Django 3.2.8 on 2021-10-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0018_rename_dnssecuritysatus_icannmodel_dnssecuritystatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='icannmodel',
            name='ActionId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icannmodel',
            name='OrderId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
