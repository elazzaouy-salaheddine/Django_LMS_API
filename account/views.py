from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .models import UserProfile
from .forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from .forms import UserProfileUpdateForm
class StudentRegistrationView(View):
    template_name = "registration/student_registration.html"
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user, is_student=True)
            return redirect("student-dashboard")
        return render(request, self.template_name, {"form": form})


class InstructorRegistrationView(View):
    template_name = "registration/instructor_registration.html"
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user, is_student=True)
            login(request, user)
            return redirect("instructor:instructor-dashboard")
        return render(request, self.template_name, {"form": form})


class AdminRegistrationView(View):
    template_name = "registration/admin_registration.html"
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user, is_student=True)
            login(request, user)
            return redirect("admin-dashboard")
        return render(request, self.template_name, {"form": form})




class InstructorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "instructor_dashboard.html"

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "admin_dashboard.html"

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profile/userprofile_detail.html'
    context_object_name = 'profile'
    def get_object(self, queryset=None):
        user_id = self.kwargs.get('user_id')
        return UserProfile.objects.get(user__id=user_id)


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileUpdateForm
    template_name = 'profile/userprofile_form.html'

    def get_object(self, queryset=None):
        # Retrieve the UserProfile associated with the logged-in user
        return UserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        user_profile = self.object  # UserProfile instance
        user = user_profile.user  # User instance associated with UserProfile
        user.username = form.cleaned_data['username']
        user.email = form.cleaned_data['email']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse('account_user:userprofile-detail', kwargs={'user_id': user_id})