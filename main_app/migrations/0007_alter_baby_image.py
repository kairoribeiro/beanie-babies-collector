# Generated by Django 4.1 on 2022-08-09 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_baby_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]
