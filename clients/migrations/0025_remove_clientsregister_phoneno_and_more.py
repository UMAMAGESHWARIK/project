# Generated by Django 4.0.7 on 2024-03-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0024_clientrequirement_finalapprove'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientsregister',
            name='phoneno',
        ),
        migrations.AddField(
            model_name='clientsregister',
            name='contact',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
