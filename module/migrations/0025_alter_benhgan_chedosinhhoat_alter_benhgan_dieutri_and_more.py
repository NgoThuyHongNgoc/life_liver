# Generated by Django 4.1.2 on 2023-01-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0024_benhgan_tenbenh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benhgan',
            name='cheDoSinhHoat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='dieuTri',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='nguyCo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='nguyenNhan',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='timHieuChung',
            field=models.TextField(null=True),
        ),
    ]
