# Generated by Django 4.1.2 on 2023-01-28 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0037_alter_tintuc_ngaydang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='khachhang',
            name='ngaySinh',
        ),
    ]
