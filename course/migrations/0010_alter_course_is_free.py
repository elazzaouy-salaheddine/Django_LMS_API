# Generated by Django 4.2.6 on 2023-10-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0009_alter_module_options_module_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="is_free",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Check if the course is free",
                null=True,
            ),
        ),
    ]
