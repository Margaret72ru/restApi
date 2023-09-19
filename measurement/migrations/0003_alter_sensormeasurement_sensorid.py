# Generated by Django 3.2.20 on 2023-09-19 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20230919_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensormeasurement',
            name='sensorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
    ]
