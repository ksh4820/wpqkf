# Generated by Django 2.1.1 on 2019-08-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_remove_photo_hitcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='timeline_photo/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='photo',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='timeline_photo/%Y/%m/%d'),
        ),
    ]
