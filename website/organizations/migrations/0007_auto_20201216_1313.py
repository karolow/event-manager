# Generated by Django 3.1.4 on 2020-12-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_organization_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='short_name',
            field=models.CharField(max_length=14),
        ),
    ]
