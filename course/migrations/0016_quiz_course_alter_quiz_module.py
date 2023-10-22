# Generated by Django 4.2.6 on 2023-10-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0015_quiz_created_at_quiz_order_quiz_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="course",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizzes_course",
                to="course.course",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="quiz",
            name="module",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizzes_module",
                to="course.module",
            ),
        ),
    ]
