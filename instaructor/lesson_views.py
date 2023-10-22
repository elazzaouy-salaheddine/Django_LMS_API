# views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from course.models import Course, Module, Lesson
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .lesson_forms import LessonForm 
from django.contrib import messages

class LessonListView(ListView):
    model = Lesson
    template_name = 'instructor_dashboard/lesson/lesson_list.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        # Get the module related to the URL parameters
        module = get_object_or_404(Module, course_id=self.kwargs['course_pk'], pk=self.kwargs['module_pk'])
        return Lesson.objects.filter(module=module)

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'instructor_dashboard/lesson/lesson_detail.html'
    context_object_name = 'lesson'

    def get_queryset(self):
        # Get the module related to the URL parameters
        module = get_object_or_404(Module, course_id=self.kwargs['course_pk'], pk=self.kwargs['module_pk'])

        return Lesson.objects.filter(module=module)


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'instructor_dashboard/lesson/lesson_form.html'

    def form_valid(self, form):
        form.instance.instructor = self.request.user 
        form.instance.module = self.get_module()

        return super().form_valid(form)

    def get_module(self):
        course_pk = self.kwargs['course_pk']
        module_pk = self.kwargs['module_pk']
        return Module.objects.get(course_id=course_pk, pk=module_pk)

    def get_success_url(self):
        messages.success(self.request, "Lesson created successfully.")
        return reverse('instructor:module-detail', kwargs={'course_pk': self.kwargs['course_pk'], 'pk': self.kwargs['module_pk']})


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm  # Use the LessonForm for lesson updates
    template_name = 'instructor_dashboard/lesson/lesson_form.html'

    def form_valid(self, form):
        form.instance.instructor = self.request.user 
        form.instance.module = self.get_module()
        return super().form_valid(form)
    def get_module(self):
        course_pk = self.kwargs['course_pk']
        module_pk = self.kwargs['module_pk']
        return Module.objects.get(course_id=course_pk, pk=module_pk)
    def get_success_url(self):
        messages.success(self.request, "Lesson updated successfully.")
        return reverse('instructor:module-detail', kwargs={'course_pk': self.kwargs['course_pk'], 'pk': self.kwargs['module_pk']})

class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'instructor_dashboard/lesson/lesson_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Lesson deleted successfully.")
        return reverse('instructor:module-detail', kwargs={'course_pk': self.kwargs['course_pk'], 'pk': self.kwargs['module_pk']})