# Generated by Django 2.2.12 on 2020-10-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('massage', models.CharField(default='', max_length=250)),
            ],
        ),
    ]
