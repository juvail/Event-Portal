# Generated by Django 3.2.4 on 2021-06-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventdetail_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetail',
            name='event_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
