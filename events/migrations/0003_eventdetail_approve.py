# Generated by Django 3.2.4 on 2021-06-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_eventdetail_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetail',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
