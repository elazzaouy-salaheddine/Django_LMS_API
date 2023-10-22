from django.urls import path
from .views import UserProfileList, UserProfileDetail, CourseList

urlpatterns = [
    path('userprofiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('userprofiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('courses/', CourseList.as_view(), name='courses-list'),
]
