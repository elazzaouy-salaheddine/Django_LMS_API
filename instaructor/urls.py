from django.urls import path
from . import views
from .module_views import (
    ModuleListView,
    ModuleDetailView,
    ModuleCreateView,
    ModuleUpdateView,
    ModuleDeleteView,
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
]
