# Generated by Django 3.2.6 on 2021-09-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DomainSearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dns',
            name='DnsTlds',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
