# Generated by Django 3.2.9 on 2021-11-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0003_alter_episode_guid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='guid',
            field=models.CharField(max_length=200, verbose_name='Guid'),
        ),
    ]