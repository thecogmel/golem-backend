# Generated by Django 4.2 on 2023-09-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hives", "0002_rename_hives_hive"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hive",
            name="status",
            field=models.CharField(
                choices=[
                    ("HEALTHY", "Healthy"),
                    ("DECLINING", "Declining"),
                    ("DEAD_OR_ABANDONED", "Dead or Abandoned"),
                ],
                default="HEALTHY",
                max_length=30,
                verbose_name="Status",
            ),
        ),
    ]
