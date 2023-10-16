from django.urls import path
from . import views

urlpatterns = [
        path('', views.StudentDashboardView.as_view(), name='student-dashboard'),

]