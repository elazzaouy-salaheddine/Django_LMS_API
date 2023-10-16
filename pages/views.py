from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import UserProfile
# Create your views here.


def index(request):
    return render(request, 'home.html')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile = UserProfile.objects.get(user_id=user.id)

        role_dashboard_mapping = {
            'student': 'student-dashboard',
            'instructor': 'instructor-dashboard',
            'admin': 'admin-dashboard'
        }

        role = ''
        if user_profile.is_student:
            role = 'student'
        elif user_profile.is_instructor:
            role = 'instructor'
        elif user_profile.is_admin:
            role = 'admin'
        return redirect(role_dashboard_mapping.get(role, 'home.html'))
    else :
        return render(request, 'home.html')
