"""
Urls for posts app
"""

from django.urls import path
from applications.posts import views as posts_views

urlpatterns = [

    path('home/', posts_views.HomeView.as_view(), name='home')
]