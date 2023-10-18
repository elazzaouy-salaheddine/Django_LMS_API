from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from course.models import Course, Module, Lesson
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for modules and lessons'

    def handle(self, *args, **options):
        # Create some fake modules and lessons
        for _ in range(10):  # Adjust the number as needed
            course = Course.objects.order_by('?').first()  # Get a random course
            module = Module.objects.create(
                course=course,
                module_name=fake.catch_phrase(),
                description=fake.paragraph()
            )
            for _ in range(random.randint(1, 5)):  # Adjust the number of lessons as needed
                Lesson.objects.create(
                    instructor=User.objects.order_by('?').first(),  # Get a random instructor
                    module=module,
                    lesson_name=fake.sentence(),
                    content=fake.text(),
                    video=fake.file_path(extension='mp4') if random.choice([True, False]) else '',
                    attachment=fake.file_path(extension='pdf') if random.choice([True, False]) else ''
                )

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully.'))
