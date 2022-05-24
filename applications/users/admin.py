from django.contrib import admin
from applications.users import models

# Register your models here.

@admin.register(models.Profile)
class AdminUsers(admin.ModelAdmin):
    pass