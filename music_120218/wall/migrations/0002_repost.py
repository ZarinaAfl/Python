# Generated by Django 2.0.3 on 2018-03-26 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='src', to='wall.Post')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reposts', to='wall.Post')),
            ],
        ),
    ]