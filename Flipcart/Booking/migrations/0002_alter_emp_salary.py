# Generated by Django 5.1.4 on 2025-01-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='salary',
            field=models.FloatField(max_length=10),
        ),
    ]
