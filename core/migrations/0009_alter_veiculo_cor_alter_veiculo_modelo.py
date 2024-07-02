# Generated by Django 5.0.6 on 2024-07-02 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_veiculo_cor_alter_veiculo_modelo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veiculo",
            name="cor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="veiculos", to="core.cor"
            ),
        ),
        migrations.AlterField(
            model_name="veiculo",
            name="modelo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="veiculos", to="core.modelo"
            ),
        ),
    ]