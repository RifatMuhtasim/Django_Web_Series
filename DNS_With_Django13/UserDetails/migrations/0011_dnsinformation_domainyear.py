# Generated by Django 3.2.6 on 2021-09-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0010_auto_20210915_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnsinformation',
            name='DomainYear',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
