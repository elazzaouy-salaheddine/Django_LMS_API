from django.urls import path
from . import views

urlpatterns = [
        path('', views.InstructorDashboardView.as_view(), name='instructor-dashboard'),

]