# Generated by Django 4.2.6 on 2023-10-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0017_alter_module_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="is_published",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
