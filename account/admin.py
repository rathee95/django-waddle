from django.contrib import admin
from .models import MyUser


@admin.register(MyUser)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_active','is_superuser','username']
# Register your models here.
