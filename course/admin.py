from django.contrib import admin
from .models import Course, Lesson, Module , Quiz, Question, Choice # Import your Course model
from django.contrib.auth.models import User  # Import User model for the instructor relationship

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor_username', 'created_at', 'updated_at']

    def instructor_username(self, obj):
        return obj.instructor.username

    instructor_username.short_description = 'Instructor'

admin.site.register(Course, CourseAdmin)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['module_name', 'course']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['lesson_name', 'module']




class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of choice fields to display for each question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of question fields to display for each quiz

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register your models with the admin site
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

