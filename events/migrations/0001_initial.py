# Generated by Django 3.2.14 on 2023-02-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('max_attendees', models.IntegerField(null=True)),
                ('start_time', models.DateTimeField(choices=[])),
                ('duration', models.DurationField(null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Upcoming'), (2, 'Past')], default=0)),
            ],
        ),
    ]
