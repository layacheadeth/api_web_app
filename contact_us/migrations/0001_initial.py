# Generated by Django 3.1.7 on 2021-06-21 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True, default=0)),
                ('realtor_email', models.EmailField(blank=True, max_length=100)),
            ],
        ),
    ]
