# Generated by Django 4.0.7 on 2024-03-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0025_remove_clientsregister_phoneno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsregister',
            name='contact',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
