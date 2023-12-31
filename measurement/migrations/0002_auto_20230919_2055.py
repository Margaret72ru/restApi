# Generated by Django 3.2.20 on 2023-09-19 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatureValue', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sensorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
        ),
        migrations.DeleteModel(
            name='TemperatureDimension',
        ),
    ]
