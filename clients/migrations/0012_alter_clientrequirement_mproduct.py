# Generated by Django 4.0.7 on 2023-12-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_alter_clientrequirement_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequirement',
            name='mProduct',
            field=models.CharField(max_length=50, null=True),
        ),
    ]