from django import forms
from course.models import Quiz, Course, Module

class QuizCreateForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'number_of_questions', 'time_limit_minutes', 'is_published','order']

