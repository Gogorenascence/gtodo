# Generated by Django 4.1.2 on 2022-10-25 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0003_alter_project_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("name", models.CharField(max_length=100)),
                ("number", models.CharField(max_length=20)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
