# Generated by Django 4.0.5 on 2022-06-30 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_cards',
            name='exp_date',
            field=models.DateField(auto_now=True),
        ),
    ]