# Generated by Django 2.2.3 on 2019-07-26 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20190726_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500, unique=True, verbose_name='password'),
        ),
    ]
