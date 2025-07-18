# Generated by Django 5.1.7 on 2025-07-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("date", models.DateField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("income", "수입"), ("expense", "지출")], max_length=10
                    ),
                ),
                ("category", models.CharField(max_length=50)),
                ("amount", models.IntegerField()),
                ("memo", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
