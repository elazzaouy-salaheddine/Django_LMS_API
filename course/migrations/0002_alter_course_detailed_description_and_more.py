# Generated by Django 4.2.6 on 2023-10-17 10:41

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="detailed_description",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="course",
            name="requirements",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="course",
            name="targeted_audience",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="course",
            name="what_youll_learn",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
    ]
