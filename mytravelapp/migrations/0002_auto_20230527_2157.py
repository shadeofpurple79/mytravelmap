# Generated by Django 3.2.19 on 2023-05-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytravelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
