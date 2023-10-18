from django.urls import path
from . import views
app_name = 'instructor'
urlpatterns = [
        path('', views.InstructorDashboardView.as_view(), name='instructor-dashboard'),
        path('courses/', views.InstructorCoursesView.as_view(), name='instructor_courses'),
        path('courses/<int:pk>/', views.InstructorCourseDetailView.as_view(), name='instructor_course_detail'),
        path('courses/<int:pk>/update/', views.InstructorCourseUpdateView.as_view(), name='instructor_course_update'),

]