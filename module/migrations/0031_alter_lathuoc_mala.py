# Generated by Django 4.1.2 on 2023-01-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0030_lathuoc_mala'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lathuoc',
            name='maLa',
            field=models.CharField(max_length=255),
        ),
    ]
