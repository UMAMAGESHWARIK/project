# Generated by Django 4.0.7 on 2023-12-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0020_clienttrequirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientrequirement',
            name='reportapprove',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clientrequirement',
            name='reportreject',
            field=models.BooleanField(default=False),
        ),
    ]
