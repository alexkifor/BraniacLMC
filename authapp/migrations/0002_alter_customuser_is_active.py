# Generated by Django 3.2.16 on 2023-01-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Required. 150 characters or fewer. ASCII letters and digits only.",
                verbose_name="active",
            ),
        ),
    ]
