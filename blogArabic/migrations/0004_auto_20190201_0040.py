# Generated by Django 2.0.9 on 2019-01-31 23:40

import blogArabic.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogArabic', '0003_auto_20190201_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myltiimage',
            name='image',
            field=models.ImageField(upload_to=blogArabic.models.get_image_filename, verbose_name='Image'),
        ),
    ]
