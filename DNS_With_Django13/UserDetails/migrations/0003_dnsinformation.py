# Generated by Django 3.2.6 on 2021-09-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0002_auto_20210914_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='DnsInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DnsTime', models.CharField(max_length=50)),
                ('DnsPrivacy', models.CharField(max_length=50)),
                ('DnsSsl', models.CharField(max_length=50)),
                ('DnsPrimum', models.CharField(max_length=50)),
                ('DnsName', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=50)),
            ],
        ),
    ]