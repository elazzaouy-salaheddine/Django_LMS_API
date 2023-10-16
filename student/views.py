from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class StudentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "student_dashboard/student_dashboard.html"