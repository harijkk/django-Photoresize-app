# Generated by Django 3.1.2 on 2020-10-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xams', '0005_auto_20201003_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xam',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
