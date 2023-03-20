# Generated by Django 3.2.14 on 2023-03-20 12:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Event Categories',
            },
        ),
        migrations.CreateModel(
            name='EventInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('max_attendees', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField()),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Upcoming'), (2, 'Past')], default=0)),
                ('attendees', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='events', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.eventcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='booker', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='events.eventcategory')),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.eventinstance')),
            ],
        ),
    ]
