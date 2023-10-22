from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from course.models import Module, Course, Quiz
from .module_form import ModuleForm

class ModuleListView(ListView):
    model = Module
    template_name = 'instructor_dashboard/module/module_list.html'
    context_object_name = 'modules'

class ModuleDetailView(DetailView):
    model = Module
    template_name = 'instructor_dashboard/module/module_detail.html'
    context_object_name = 'module'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve related quizzes for the module
        context['quizzes'] = Quiz.objects.filter(module=self.object)
        
        return context
class ModuleMixin:
    model = Module
    form_class = ModuleForm
    template_name = 'instructor_dashboard/module/module_form.html'

    def get_course(self):
        course_pk = self.kwargs['course_pk']
        return Course.objects.get(pk=course_pk)

class ModuleCreateView(ModuleMixin, CreateView):
    def form_valid(self, form):
        form.instance.course = self.get_course()
        messages.success(self.request, "Module created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('instructor:instructor_course_detail', kwargs={'pk': self.object.course.pk})

class ModuleUpdateView(ModuleMixin, UpdateView):
    def get_success_url(self):
        messages.success(self.request, "Module updated successfully.")
        return reverse('instructor:instructor_course_detail', kwargs={'pk': self.object.course.pk})

class ModuleDeleteView(DeleteView):
    model = Module
    template_name = 'instructor_dashboard/module/module_confirm_delete.html'
    def get_success_url(self):
        messages.success(self.request, "Module delete successfully.")
        return reverse('instructor:instructor_course_detail', kwargs={'pk': self.object.course.pk})

