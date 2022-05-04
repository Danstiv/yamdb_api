# Generated by Django 2.2.16 on 2022-05-04 07:44

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220504_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.models.no_future_year]),
        ),
    ]
