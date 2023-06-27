from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_created')
    list_display_links = ('email', 'username', 'first_name',)


admin.site.register(User, UserAdmin)
