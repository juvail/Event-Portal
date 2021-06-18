# Generated by Django 3.2.4 on 2021-06-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('event_image', models.ImageField(upload_to='media/events')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('venue', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=700, null=True)),
            ],
        ),
    ]