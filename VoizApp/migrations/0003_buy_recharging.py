# Generated by Django 4.0.5 on 2022-07-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoizApp', '0002_dongle_invoice_issue_postpaid_prepaid_recharge'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(help_text='mm/dd/yy Hour:Min')),
                ('type', models.CharField(choices=[('prepaid', 'Prepaid'), ('postpaid', 'Postpaid'), ('dongle', 'Dongle')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='recharging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(max_length=11)),
                ('type', models.CharField(choices=[('prepaid', 'Prepaid'), ('postpaid', 'Postpaid'), ('dongle', 'Dongle')], max_length=9)),
                ('amt', models.IntegerField()),
            ],
        ),
    ]