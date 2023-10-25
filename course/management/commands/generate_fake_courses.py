import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from course.models import Course  # Replace 'yourapp' with the actual app name where your models are defined
import random
from django.contrib.auth.models import User  # Import the User model
from django.core.files import File
from django.db.models.fields.files import ImageField, FileField
from django.core.management.base import BaseCommand
from django.db.models import FileField

from course.models import Course , upload_to_course_video # Import your Course model

class Command(BaseCommand):
    help = 'Generate fake data for the Course model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create a list of language choices and difficulty level choices
        LANGUAGE_CHOICES = ['en', 'es', 'fr', 'de', 'it']
        DIFFICULTY_LEVEL_CHOICES = ['beginner', 'intermediate', 'advanced']

        for _ in range(10):  # Create 10 fake Course instances
            course = Course(
                title=fake.sentence(nb_words=4),
                excerpt=fake.text(max_nb_chars=200),
                instructor=User.objects.order_by('?').first(),  # Random instructor
                language=random.choice(LANGUAGE_CHOICES),
                is_certified=fake.boolean(),
                image_thumbnail=f'https://picsum.photos/400/300/?random={fake.random_int(min=1, max=1000)}',                price=fake.random_int(min=10, max=100),
                what_youll_learn=fake.text(max_nb_chars=400),
                requirements=fake.text(max_nb_chars=200),
                detailed_description=fake.text(max_nb_chars=1000),
                difficulty_level=random.choice(DIFFICULTY_LEVEL_CHOICES),
                is_public=fake.boolean(),
                is_published=fake.boolean(),
                video_intro=FileField(upload_to=upload_to_course_video).attr_class(None, FileField(upload_to=upload_to_course_video), None),
            )
            course.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data for the Course model.'))
