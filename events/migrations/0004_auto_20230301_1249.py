# Generated by Django 3.2.14 on 2023-03-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20230228_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinstance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='eventinstance',
            name='start_time',
            field=models.TimeField(choices=[]),
        ),
    ]
