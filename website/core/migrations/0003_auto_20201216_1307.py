# Generated by Django 3.1.4 on 2020-12-16 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='type',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='type',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
