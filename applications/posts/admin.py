from django.contrib import admin
# Models
from applications.posts import models
# Register your models here.

@admin.register(models.Posts)
class AdminPosts(admin.ModelAdmin):
    pass