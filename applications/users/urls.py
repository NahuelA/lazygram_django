"""
Urls for users app
"""

from django.urls import path
from applications.users.views import (
    # Login and logout views
    login_view,
    logout_view,
    # CRUD views
    UserSignUpView,
    ProfileSignUpView,
    ProfileUpdateView,
    ProfileView,

)
urlpatterns = [

    # Login
    path(route ='accounts/login',
         view =login_view,
         name='login'
        ),
    
    path(route ='accounts/logout', 
         view=logout_view, 
         name='logout'),

    # CRUD
    # Create
    path(route ='accounts/register', 
         view=UserSignUpView.as_view(), 
         name='user-create'),

    path(route ='accounts/register/profile', 
         view=ProfileSignUpView.as_view(), 
         name='profile-create'),

    # Read
    path(route ='accounts/profile', 
         view=ProfileView.as_view() ,
         name='profile-view'),

    # Update
    path(route ='accounts/profile/update/<slug:slug>/<int:pk>/', 
         view=ProfileUpdateView.as_view(), 
         name='profile-update')
]