# Generated by Django 3.2.8 on 2021-10-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0015_auto_20210922_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpersonalinformation',
            old_name='Address',
            new_name='Address1',
        ),
        migrations.AddField(
            model_name='userpersonalinformation',
            name='Address2',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpersonalinformation',
            name='ContactId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpersonalinformation',
            name='PhoneCode',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpersonalinformation',
            name='ZipCode',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
