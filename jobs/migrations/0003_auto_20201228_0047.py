# Generated by Django 3.0.7 on 2020-12-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20201227_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]