# Generated by Django 3.1.1 on 2020-09-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.ImageField(max_length=10, unique=True, upload_to=''),
        ),
    ]
