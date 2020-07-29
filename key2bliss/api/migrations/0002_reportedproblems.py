# Generated by Django 3.0.6 on 2020-07-29 17:08

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedProblems',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('full_name', models.TextField()),
                ('email', models.EmailField(error_messages={'unique': 'This email address is already taken.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.core.validators.EmailValidator])),
                ('message', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
