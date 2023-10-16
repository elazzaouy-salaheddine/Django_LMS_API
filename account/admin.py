from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_student', 'is_instructor', 'is_admin')
    list_filter = ('is_student', 'is_instructor', 'is_admin')
    search_fields = ('user__username', 'user__email')

# Register the UserProfile model with the admin site
admin.site.register(UserProfile, UserProfileAdmin)