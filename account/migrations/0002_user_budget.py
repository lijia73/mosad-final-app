# Generated by Django 3.1.4 on 2020-12-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Budget',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]