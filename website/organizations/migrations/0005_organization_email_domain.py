# Generated by Django 3.1.4 on 2020-12-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20201105_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='email_domain',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
