# Generated by Django 4.2.6 on 2023-10-17 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "title",
                    models.CharField(
                        help_text="Enter the title of the course.", max_length=255
                    ),
                ),
                (
                    "excerpt",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en", "English"),
                            ("es", "Spanish"),
                            ("fr", "French"),
                            ("de", "German"),
                            ("it", "Italian"),
                        ],
                        help_text="Enter the language of the course.",
                        max_length=50,
                    ),
                ),
                (
                    "is_certified",
                    models.BooleanField(
                        default=False, help_text="Check if the course is certified."
                    ),
                ),
                (
                    "is_free",
                    models.BooleanField(
                        default=False, help_text="Check if the course is free."
                    ),
                ),
                (
                    "has_video_intro",
                    models.BooleanField(
                        default=False,
                        help_text="Check if the course has a video introduction.",
                    ),
                ),
                (
                    "image_thumbnail",
                    models.ImageField(
                        help_text="Upload an image thumbnail for the course.",
                        upload_to="course_thumbnails/",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Enter the price of the course.",
                        max_digits=10,
                        null=True,
                    ),
                ),
                (
                    "what_youll_learn",
                    models.TextField(
                        help_text="Enter what the students will learn in the course."
                    ),
                ),
                (
                    "requirements",
                    models.TextField(
                        help_text="Enter the requirements for the course."
                    ),
                ),
                (
                    "detailed_description",
                    models.TextField(
                        help_text="Enter a detailed description of the course."
                    ),
                ),
                (
                    "difficulty_level",
                    models.CharField(
                        choices=[
                            ("beginner", "Beginner"),
                            ("intermediate", "Intermediate"),
                            ("advanced", "Advanced"),
                        ],
                        max_length=20,
                    ),
                ),
                ("is_public", models.BooleanField(default=False)),
                ("targeted_audience", models.CharField(max_length=255)),
                (
                    "instructor",
                    models.ForeignKey(
                        help_text="Select the instructor of the course.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="courses_taught",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
            },
        ),
    ]
