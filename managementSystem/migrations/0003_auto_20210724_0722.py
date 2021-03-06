# Generated by Django 3.2.5 on 2021-07-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementSystem', '0002_auto_20210723_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='water_prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time_d', models.TimeField(auto_now=True)),
                ('volume_d', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.AlterField(
            model_name='energy_saver',
            name='powerMain',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='energy_saver',
            name='powerSun',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
