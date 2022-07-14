# Generated by Django 4.0.5 on 2022-07-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoizApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dongle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(max_length=100)),
                ('data_day', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='postpaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(max_length=100)),
                ('total_data', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='prepaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(max_length=100)),
                ('data_day', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='recharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(max_length=11)),
                ('plan', models.CharField(max_length=100)),
                ('amt', models.IntegerField(max_length=10)),
            ],
        ),
    ]