import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from course.models import Course  # Replace 'yourapp' with the actual app name where your models are defined

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake course data'

    def handle(self, *args, **options):
        # Retrieve a list of existing users who can be instructors
        instructors = User.objects.filter(is_superuser=False)

        for _ in range(10):  # Generate 10 fake courses as an example, you can adjust the number
            title = fake.catch_phrase()
            excerpt = fake.paragraph()
            instructor = random.choice(instructors)
            language = random.choice([choice[0] for choice in Course.LANGUAGE_CHOICES])
            is_certified = fake.boolean()
            is_free = fake.boolean()
            price = round(random.uniform(10, 1000), 2)
            video_intro = 'path_to_video.mp4'  # Replace with a path to your video file
            image_thumbnail = 'path_to_thumbnail.jpg'  # Replace with a path to your image file
            what_youll_learn = fake.text()
            requirements = fake.text()
            detailed_description = fake.text()
            difficulty_level = random.choice([choice[0] for choice in Course.DIFFICULTY_LEVEL_CHOICES])
            is_public = fake.boolean()
            targeted_audience = fake.text()

            Course.objects.create(
                title=title,
                excerpt=excerpt,
                instructor=instructor,
                language=language,
                is_certified=is_certified,
                is_free=is_free,
                price=price,
                video_intro=video_intro,
                image_thumbnail=image_thumbnail,
                what_youll_learn=what_youll_learn,
                requirements=requirements,
                detailed_description=detailed_description,
                difficulty_level=difficulty_level,
                is_public=is_public,
                targeted_audience=targeted_audience
            )

        self.stdout.write(self.style.SUCCESS('Fake courses have been generated.'))
