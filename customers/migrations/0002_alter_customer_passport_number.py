# Generated by Django 4.2.7 on 2024-01-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="passport_number",
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
