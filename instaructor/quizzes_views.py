from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from course.models import Quiz, Module, Course
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse
class QuizListView(ListView):
    model = Quiz
    template_name = 'instructor_dashboard/quiz/quiz_list.html'
    context_object_name = 'quizzes'  # Optional, the context variable name in the template




class QuizCreateView(CreateView):
    model = Quiz
    template_name = 'instructor_dashboard/quiz/quiz_form.html'
    fields = ['title', 'description', 'number_of_questions', 'time_limit_minutes', 'is_published','order']

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        form.instance.course = self.get_course()
        form.instance.module = self.get_module()
        return super().form_valid(form)

    def get_course(self):
        # Implement logic to get the course based on your requirements.
        # You can use self.kwargs, self.request, or any other method to retrieve the course.
        # For example:
        # course_id = self.kwargs['course_id']
        # return Course.objects.get(pk=course_id)
        pass

    def get_module(self):
        course_pk = self.kwargs['course_pk']
        module_pk = self.kwargs['module_pk']
        return Module.objects.get(course_id=course_pk, pk=module_pk)

    def get_success_url(self):
        return reverse('instructor:quiz-detail', 
                kwargs={
                        'course_pk': self.kwargs['course_pk'], 
                        'module_pk': self.kwargs['module_pk'],
                        'quiz_pk': self.object.pk})


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'instructor_dashboard/quiz/quiz_detail.html'
    context_object_name = 'quiz'

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs['quiz_pk'])

    def get_queryset(self):
        module = get_object_or_404(Module, course_id=self.kwargs['course_pk'], pk=self.kwargs['module_pk'])
        return Quiz.objects.filter(module=module)


class QuizUpdateView(UpdateView):
    model = Quiz
    fields = ['title', 'description', 'number_of_questions', 'time_limit_minutes', 'is_published']
    template_name = 'instructor_dashboard/quiz/quiz_form.html'
    success_url = '/quiz/list/'  # URL to redirect to upon successful update




class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'instructor_dashboard/quiz/quiz_confirm_delete.html'
    success_url = '/quiz/list/'  # URL to redirect to upon successful deletion
