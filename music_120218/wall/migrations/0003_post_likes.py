# Generated by Django 2.0.3 on 2018-04-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_repost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Нравится'),
        ),
    ]
