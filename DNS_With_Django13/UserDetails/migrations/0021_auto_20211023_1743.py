# Generated by Django 3.2.8 on 2021-10-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0020_auto_20211023_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icannmodel',
            old_name='ContactId',
            new_name='AdContactId',
        ),
        migrations.AddField(
            model_name='icannmodel',
            name='CustomerId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icannmodel',
            name='ReContactId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
