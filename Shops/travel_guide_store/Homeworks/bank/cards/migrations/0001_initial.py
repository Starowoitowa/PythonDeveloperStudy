# Generated by Django 4.0.5 on 2022-07-22 07:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('iban', models.UUIDField(default=uuid.UUID('c62fa4d0-ee2d-4551-8dad-082520b02c5d'), primary_key=True, serialize=False)),
                ('sum', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('uuid', models.UUIDField(default=uuid.UUID('aad122b5-7aa2-4fb1-9b8d-c94f002510eb'), primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveBigIntegerField(max_length=16)),
                ('expiration_date', models.DateField(default=datetime.date(2025, 7, 22))),
                ('cvv', models.IntegerField(max_length=3)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.account')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.user')),
            ],
            options={
                'db_table': 'cards',
            },
        ),
    ]