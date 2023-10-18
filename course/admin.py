from django.contrib import admin
from .models import Course, Lesson, Module  # Import your Course model
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