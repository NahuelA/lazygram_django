"""
Urls for posts app
"""

from django.urls import path
from applications.posts import views as posts_views

urlpatterns = [

    path(
        route='home/',
        view=posts_views.HomeView.as_view(),
        name='home'
    ),

    path(
        route='create-post/',
        view=posts_views.CreatePostView.as_view(),
        name = 'create-post'
    )
]