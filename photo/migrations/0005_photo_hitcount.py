# Generated by Django 2.1.1 on 2019-08-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='hitcount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
