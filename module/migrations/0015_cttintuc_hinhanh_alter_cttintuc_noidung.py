# Generated by Django 4.1.2 on 2022-12-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0014_alter_tintuc_hinhanh'),
    ]

    operations = [
        migrations.AddField(
            model_name='cttintuc',
            name='hinhAnh',
            field=models.ImageField(default=False, upload_to='tintuc'),
        ),
        migrations.AlterField(
            model_name='cttintuc',
            name='noiDung',
            field=models.TextField(default=''),
        ),
    ]
