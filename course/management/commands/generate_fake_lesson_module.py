import random
from django.core.management.base import BaseCommand
from faker import Faker
from course.models import Course, Module, Lesson, Quiz, Question, Choice, upload_to_course_video
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField, FileField
class Command(BaseCommand):
    help = 'Generate fake data for various models in myapp'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate fake data for the Course model
        for _ in range(10):  # Create 10 fake courses
            course = Course(
                title=fake.sentence(nb_words=4),
                excerpt=fake.text(max_nb_chars=200),
                instructor=User.objects.order_by('?').first(),  # Replace with your user selection logic
                language=random.choice([choice[0] for choice in Course.LANGUAGE_CHOICES]),
                is_certified=fake.boolean(chance_of_getting_true=50),
                image_thumbnail=fake.url(),  # Use a URL as a placeholder for the image
                price=fake.random_int(min=10, max=100),
                what_youll_learn=fake.text(max_nb_chars=400),
                requirements=fake.text(max_nb_chars=200),
                detailed_description=fake.text(max_nb_chars=1000),
                difficulty_level=random.choice([choice[0] for choice in Course.DIFFICULTY_LEVEL_CHOICES]),
                is_public=fake.boolean(),
                is_published=fake.boolean(),
                video_intro=FileField(upload_to=upload_to_course_video).attr_class(None, FileField(upload_to=upload_to_course_video), None),
            )
            course.save()

        # Generate fake data for the Module model
        for course in Course.objects.all():
            for order in range(1, 6):  # Create 5 fake modules for each course
                module = Module(
                    course=course,
                    module_name=fake.word().title(),
                    description=fake.text(max_nb_chars=500),
                    order=order,
                    is_published=fake.boolean(chance_of_getting_true=70),
                )
                module.save()

        # Generate fake data for the Lesson model
        for module in Module.objects.all():
            for _ in range(5):  # Create 5 fake lessons for each module
                lesson = Lesson(
                    instructor=User.objects.order_by('?').first(),  # Replace with your user selection logic
                    module=module,
                    lesson_name=fake.sentence(nb_words=4),
                    content=fake.text(max_nb_chars=1000),
                    video=FileField(upload_to=upload_to_course_video).attr_class(None, FileField(upload_to=upload_to_course_video), None),
                    attachment=FileField(upload_to='course_attachments/').attr_class(None, FileField(upload_to='course_attachments/'), None),
                    is_published=fake.boolean(chance_of_getting_true=70),
                )
                lesson.save()

        # Repeat similar steps for the Quiz, Question, and Choice models

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data for various models.'))
