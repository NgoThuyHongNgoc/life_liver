# Generated by Django 4.1.2 on 2022-12-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0017_rename_makhachhang_donhang_sdtkhachhang_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donhang',
            name='diaChi',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='donhang',
            name='tenKhachHang',
            field=models.CharField(max_length=255),
        ),
    ]
