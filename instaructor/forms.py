from django import forms
from course.models import Course

class CourseForm(forms.ModelForm):

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
    class Meta:
        model = Course
        exclude = ['instructor']
    title = forms.CharField(
        label='Course Title',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
        help_text="Enter the price of the course"
    )

    image_thumbnail = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        help_text="Upload an image thumbnail for the course"
    )

    difficulty_level = forms.ChoiceField(
        choices=Course.DIFFICULTY_LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Select the difficulty level of the course"
    )
    language = forms.ChoiceField(
        choices=Course.LANGUAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Select the language of the course"
    )


