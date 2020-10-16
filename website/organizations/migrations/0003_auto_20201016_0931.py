# Generated by Django 3.1.2 on 2020-10-16 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201016_0931'),
        ('organizations', '0002_activity_organization'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Organizations',
        ),
        migrations.AddField(
            model_name='activity',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization'),
        ),
    ]
