from django.contrib.auth.views import (
    LoginView,
    LogoutView, PasswordChangeView, 
    PasswordChangeDoneView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView, 
    PasswordResetCompleteView)
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
app_name = 'account_user'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login_account'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout_account'),

    path('password-change/', PasswordChangeView.as_view(
                                template_name='account/password_change_form.html',
                                form_class=PasswordChangeForm,
                                success_url='account_user:password_reset_done'
                                ), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
                                                    template_name='account/password_change_done.html',),  
                                                    name='password_change_done'),

    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset_form.html', 
                                                    form_class=PasswordResetForm,
                                                    email_template_name='account/password_reset_email.html'), 
                                                    name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
                            template_name='account/password_reset_done.html'), 
                            name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
                            template_name='account/password_reset_confirm.html', 
                            form_class=SetPasswordForm), 
                            name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('student-registration/', views.StudentRegistrationView.as_view(), 
                        name='student-registration'),
    path('instructor-registration/', views.InstructorRegistrationView.as_view(), 
                        name='instructor-registration'),
    path('admin-registration/', views.AdminRegistrationView.as_view(), 
        name='admin-registration'),

    path('profile/<int:user_id>/', views.UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('profile/edit/', views.UserProfileUpdateView.as_view(), name='userprofile-update'),

]