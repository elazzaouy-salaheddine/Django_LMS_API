from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field



def upload_to_course_video(instance, filename):
    # Get the username of the instructor and the title of the course
    instructor_username = instance.instructor.username
    course_title = instance.title
    # Create the upload path based on the instructor's username and course title
    return f'course_videos/{instructor_username}/{course_title}/{filename}'

class Course(models.Model):
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

    title = models.CharField(max_length=255, blank=False, null=False, help_text="Enter the title of the course.")
    excerpt = CKEditor5Field('Text', config_name='extends')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught', blank=False, null=False, help_text="Select the instructor of the course.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, help_text="Enter the language of the course.")
    is_certified = models.BooleanField(default=False, help_text="Check if the course is certified.")
    is_free = models.BooleanField(default=False, help_text="Check if the course is free.")
    video_intro = models.FileField(
        upload_to=upload_to_course_video,
        help_text="Upload a video intro for the course. (e.g., MP4, AVI, MOV)",
        null=True,
        blank=True
    )    
    image_thumbnail = models.ImageField(upload_to='course_thumbnails/', help_text="Upload an image thumbnail for the course.")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Enter the price of the course.")
    what_youll_learn = CKEditor5Field('Text', config_name='extends')
    requirements = CKEditor5Field('Text', config_name='extends')
    detailed_description = CKEditor5Field('Text', config_name='extends')
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVEL_CHOICES, blank=False, null=False)  
    is_public = models.BooleanField(default=False)
    targeted_audience = CKEditor5Field('Text', config_name='extends')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title
