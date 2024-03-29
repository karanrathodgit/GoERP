# Generated by Django 4.2.6 on 2023-10-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RegistrationModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField(max_length=150)),
                ("project_date", models.DateField()),
                ("PO_number", models.IntegerField()),
                ("client_name", models.CharField(max_length=200)),
                ("wo_number", models.CharField(max_length=50)),
                ("projected_cost", models.IntegerField()),
                ("cdd", models.DateField()),
            ],
        ),
    ]
