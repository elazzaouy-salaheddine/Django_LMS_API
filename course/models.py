from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


# Define a reusable function to generate video upload path
def upload_to_course_video(instance, filename):
    instructor_username = instance.instructor.username
    course_title = instance.module.course.title  # Access the course title from the module
    return f'course_videos/{instructor_username}/{course_title}/{filename}'

# Choices for languages and difficulty levels
LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('de', 'German'),
    ('it', 'Italian'),
]

DIFFICULTY_LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]

class Course(models.Model):
    title = models.CharField(max_length=255, help_text="Enter the title of the course")
    excerpt = models.TextField(help_text="Enter a short course description")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, help_text="Select the course language")
    is_certified = models.BooleanField(default=False, help_text="Check if the course is certified")
    is_free = models.BooleanField(default=False, help_text="Check if the course is free")
    image_thumbnail = models.ImageField(upload_to='course_thumbnails/', help_text="Upload an image thumbnail for the course")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Enter the price of the course")
    what_youll_learn = models.TextField(help_text="Enter what students will learn")
    requirements = models.TextField(help_text="Enter course requirements")
    detailed_description = models.TextField(help_text="Enter a detailed course description")
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVEL_CHOICES)
    is_public = models.BooleanField(default=False, help_text="Check if the course is public")
    video_intro = models.FileField(upload_to=upload_to_course_video, null=True, blank=True, help_text="Upload a video intro (e.g., MP4, AVI, MOV)")

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    module_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.module_name

class Lesson(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons_taught')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    lesson_name = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to=upload_to_course_video, null=True, blank=True)
    attachment = models.FileField(upload_to='course_attachments/', null=True, blank=True)

    def __str__(self):
        return self.lesson_name