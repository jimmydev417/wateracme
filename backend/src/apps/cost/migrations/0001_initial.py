# Generated by Django 2.2.3 on 2020-01-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=100)),
                ('tariff', models.IntegerField()),
                ('date_create', models.DateField()),
                ('date_stop', models.DateField()),
                ('is_activate', models.BooleanField()),
            ],
        ),
    ]