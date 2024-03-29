# Generated by Django 4.2 on 2023-11-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hives", "0008_remove_hive_responsible_hive_q_ca_hive_q_cf_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hive",
            name="q_ca",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Quantidade de quadros com alimento",
            ),
        ),
        migrations.AlterField(
            model_name="hive",
            name="q_cf",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Quantidade de quadros com cria",
            ),
        ),
        migrations.AlterField(
            model_name="hive",
            name="q_ci",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Quantidade de quadros com insetos",
            ),
        ),
        migrations.AlterField(
            model_name="hive",
            name="q_cv",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Quantidade de quadros com vazio",
            ),
        ),
        migrations.AlterField(
            model_name="hive",
            name="q_total",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Quantidade de quadros totais",
            ),
        ),
    ]
