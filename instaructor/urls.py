from django.urls import path
from . import views
from .module_views import (
    ModuleListView,
    ModuleDetailView,
    ModuleCreateView,
    ModuleUpdateView,
    ModuleDeleteView,
)
from .lesson_views import(
    LessonDetailView, LessonDetailView,LessonCreateView, LessonDeleteView,LessonUpdateView,
)
from .quizzes_views import(
    QuizListView, QuizCreateView, QuizDeleteView, QuizUpdateView,QuizDetailView,
)
    

app_name = "instructor"
urlpatterns = [
    path("", views.InstructorDashboardView.as_view(), name="instructor-dashboard"),
    path("courses/", views.InstructorCoursesView.as_view(), name="instructor_courses"),
    path(
        "courses/<int:pk>/",
        views.InstructorCourseDetailView.as_view(),
        name="instructor_course_detail",
    ),
    path(
        "courses/<int:pk>/update/",
        views.InstructorCourseUpdateView.as_view(),
        name="instructor_course_update",
    ),
    path('courses/<int:course_pk>/modules/', ModuleListView.as_view(), name='module-list'),

    # Module detail view
    path('courses/<int:course_pk>/modules/<int:pk>/', ModuleDetailView.as_view(), name='module-detail'),

    # Create a module
    path('courses/<int:course_pk>/modules/create/', ModuleCreateView.as_view(), name='module-create'),

    # Update a module
    path('courses/<int:course_pk>/modules/<int:pk>/update/', ModuleUpdateView.as_view(), name='module-update'),

    # Delete a module
    path('courses/<int:course_pk>/modules/<int:pk>/delete/', ModuleDeleteView.as_view(), name='module-delete'),
    # URL to display an individual lesson
    path('courses/<int:course_pk>/modules/<int:module_pk>/lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('courses/<int:course_pk>/modules/<int:module_pk>/lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),
    path('courses/<int:course_pk>/modules/<int:module_pk>/lessons/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),
    path('courses/<int:course_pk>/modules/<int:module_pk>/lessons/create/', LessonCreateView.as_view(), name='lesson-create'),

    path('courses/<int:course_pk>/modules/<int:module_pk>/quizzes/create/', QuizCreateView.as_view(), name='quiz-create'),
    path('courses/<int:course_pk>/modules/<int:module_pk>/quizzes/<int:quiz_pk>/', QuizDetailView.as_view(), name='quiz-detail'),


]
