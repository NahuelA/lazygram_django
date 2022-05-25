"""
Urls for users app
"""

from django.urls import path, reverse
from applications.users.views import (
    login_view,
    logout_view,
    UserSignUpView,
    ProfileSignUpView,
    ProfileView,
)
urlpatterns = [

    # Login
    path('accounts/login', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),
    # Sign-up User and Profile information
    path('accounts/register', UserSignUpView.as_view(), name='sign-up'),
    path('accounts/profile/up', ProfileSignUpView.as_view(), name='profile-sign-up'),
    # View profile
    path('accounts/profile', ProfileView.as_view(), name='profile'),
]