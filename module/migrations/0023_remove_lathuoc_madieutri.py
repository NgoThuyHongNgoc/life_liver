# Generated by Django 4.1.2 on 2023-01-04 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0022_rename_madieutri_dieutri_mala'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lathuoc',
            name='maDieuTri',
        ),
    ]
