# Generated by Django 4.2.11 on 2024-04-04 23:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0012_alter_agendamentoexame_resultado"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agendamentoexame",
            name="resultado",
            field=models.FileField(
                blank=True, null=True, upload_to="pdfs/", verbose_name="Resultado"
            ),
        ),
    ]
