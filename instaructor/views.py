from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from course.models import Course
from .forms import CourseForm
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

class InstructorCourseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'instructor_dashboard/courses/course_form.html'
    model = Course
    form_class = CourseForm 

    def form_valid(self, form):
        # Set the instructor to the authenticated user
        form.instance.instructor = self.request.user
        messages.success(self.request, 'Course updated successfully.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Course creation failed. Please check the form.')
        return super().form_invalid(form)
    def get_success_url(self):
        # Redirect to the course details page for the updated course
        return reverse('instructor:instructor_course_detail', kwargs={'pk': self.object.pk})