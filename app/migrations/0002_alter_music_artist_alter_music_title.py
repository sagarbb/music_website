# Generated by Django 5.0.3 on 2024-03-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='music',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
