# Generated by Django 3.1.2 on 2020-10-15 13:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('location', models.CharField(max_length=255)),
                ('room', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('contact_person', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]