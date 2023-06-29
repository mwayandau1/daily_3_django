from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('-date_joined',)
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_created')
    list_display_links = ('email', 'username', 'first_name',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
