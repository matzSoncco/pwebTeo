# Generated by Django 5.0.6 on 2024-06-12 03:39

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('idAdmin', models.UUIDField(default=uuid.UUID('53523fba-286d-11ef-8d4a-ec63d7e5c5e9'), editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=10)),
                ('web_page', models.URLField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_created_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_universities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
