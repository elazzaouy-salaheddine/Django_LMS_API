# Generated by Django 4.2.6 on 2023-10-20 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("course", "0018_alter_lesson_is_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="instructor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizzes_taught",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
