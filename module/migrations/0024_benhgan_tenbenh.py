# Generated by Django 4.1.2 on 2023-01-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0023_remove_lathuoc_madieutri'),
    ]

    operations = [
        migrations.AddField(
            model_name='benhgan',
            name='tenBenh',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
