# Generated by Django 3.1.1 on 2020-09-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200909_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(null=True, unique=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(null=True, unique=True, upload_to='images'),
        ),
    ]