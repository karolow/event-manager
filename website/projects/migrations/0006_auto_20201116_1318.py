# Generated by Django 3.1.3 on 2020-11-16 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_location'),
        ('projects', '0005_auto_20201105_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.location'),
        ),
    ]
