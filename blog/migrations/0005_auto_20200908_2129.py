# Generated by Django 3.1.1 on 2020-09-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200908_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, unique=True, upload_to='images'),
        ),
    ]
