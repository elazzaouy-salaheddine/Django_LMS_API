from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse

# Define a reusable function to generate video upload path
def upload_to_course_video(instance, filename):
    instructor_username = instance.instructor.username
    course_title = instance.module.course.title  # Access the course title from the module
    return f'course_videos/{instructor_username}/{course_title}/{filename}'

# Choices for languages and difficulty levels


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
    title = models.CharField(max_length=255, help_text="Enter the title of the course")
    excerpt = RichTextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, help_text="Select the course language")
    is_certified = models.BooleanField(help_text="Check if the course is certified")
    image_thumbnail = models.ImageField(upload_to='course_thumbnails/', help_text="Upload an image thumbnail for the course")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Enter the price of the course")
    what_youll_learn = RichTextField()
    requirements = RichTextField()
    detailed_description = RichTextField()
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVEL_CHOICES)
    is_public = models.BooleanField(default=False, help_text="Check if the course is public")
    is_published = models.BooleanField()
    video_intro = models.FileField(upload_to=upload_to_course_video, null=True, blank=True, help_text="Upload a video intro (e.g., MP4, AVI, MOV)")

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    module_name = models.CharField(max_length=255)
    description = RichTextField()
    order = models.PositiveIntegerField()
    is_published = models.BooleanField(null=True, blank=True)
    class Meta:
        # Define the default ordering by the 'order' field in ascending order
        ordering = ['order']
    def __str__(self):
        return self.module_name

class Lesson(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons_taught')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    lesson_name = models.CharField(max_length=255)
    content = RichTextField()
    video = models.FileField(upload_to=upload_to_course_video, null=True, blank=True)
    attachment = models.FileField(upload_to='course_attachments/', null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    def get_absolute_url(self):
        return reverse('instructor:lesson-detail', args=[str(self.module.course.id), str(self.module.id), str(self.id)])

    def __str__(self):
        return self.lesson_name


class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='quizzes_module')
    title = models.CharField(max_length=255, help_text="Enter the title of the quiz")
    description = models.TextField()
    number_of_questions = models.PositiveIntegerField(help_text="Enter the number of questions in the quiz")
    time_limit_minutes = models.PositiveIntegerField(help_text="Enter the time limit for the quiz in minutes")
    is_published = models.BooleanField(default=False, help_text="Check if the quiz is published")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField(help_text="Enter the question text")
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255, help_text="Enter the choice text")
    is_correct = models.BooleanField(default=False, help_text="Check if this choice is correct")

    def __str__(self):
        return self.choice_text