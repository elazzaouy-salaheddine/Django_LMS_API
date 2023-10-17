from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
class InstructorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "instructor_dashboard/instructor_dashboard.html"



    