# Generated by Django 4.1.2 on 2023-01-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0025_alter_benhgan_chedosinhhoat_alter_benhgan_dieutri_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benhgan',
            name='cheDoSinhHoat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='dieuTri',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='nguyCo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='nguyenNhan',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='benhgan',
            name='timHieuChung',
            field=models.TextField(blank=True, null=True),
        ),
    ]
