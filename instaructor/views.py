from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from course.models import Course
class InstructorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "instructor_dashboard/instructor_dashboard.html"



class InstructorCoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'instructor_dashboard/courses/instructor_courses.html'  
    context_object_name = 'courses'

    def get_queryset(self):
        user = self.request.user  # Get the currently logged-in user
        return Course.objects.filter(instructor=user)

class InstructorCourseDetailView(DetailView):
    model = Course
    template_name = 'instructor_dashboard/courses/course_detail.html' 
    context_object_name = 'course'

class InstructorCourseUpdateView(UpdateView):
    model = Course
    template_name = 'instructor_dashboard/courses/course_form.html'
    fields = '__all__'  # Use all fields from the Course model