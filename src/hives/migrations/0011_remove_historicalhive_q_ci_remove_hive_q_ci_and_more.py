# Generated by Django 4.2 on 2023-11-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hives", "0010_historicalhive_historicalcollection"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalhive",
            name="q_ci",
        ),
        migrations.RemoveField(
            model_name="hive",
            name="q_ci",
        ),
        migrations.AlterField(
            model_name="historicalhive",
            name="queen_status",
            field=models.CharField(
                choices=[("REGULAR", "REGULAR"), ("GOOD", "GOOD"), ("WEAK", "WEAK")],
                default="REGULAR",
                max_length=30,
                verbose_name="Status da Rainha",
            ),
        ),
        migrations.AlterField(
            model_name="hive",
            name="queen_status",
            field=models.CharField(
                choices=[("REGULAR", "REGULAR"), ("GOOD", "GOOD"), ("WEAK", "WEAK")],
                default="REGULAR",
                max_length=30,
                verbose_name="Status da Rainha",
            ),
        ),
    ]