# Generated by Django 4.0.7 on 2023-12-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_clientsregister_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsregister',
            name='fileupload',
            field=models.FileField(default=None, upload_to='documents/'),
        ),
    ]
