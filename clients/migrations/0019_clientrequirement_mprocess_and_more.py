# Generated by Django 4.0.7 on 2023-12-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_alter_clientrequirement_ghostfishingnets'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientrequirement',
            name='MProcess',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clientrequirement',
            name='mechreport',
            field=models.BooleanField(default=False),
        ),
    ]
