# Generated by Django 3.2.9 on 2022-04-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoCodeBD', '0002_auto_20220418_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]