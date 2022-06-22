"""
Urls for users app
"""

from django.urls import path
from applications.users.views import (
    # Login and logout views
    Login,
    Logout,
    # CRUD views
    UserSignUpView,
    ProfileSignUpView,
    ProfileUpdateView,
    ProfileView,

)
urlpatterns = [

     # Login
     path(route ='accounts/login',
         view = Login.as_view(),
         name='login'
        ),
    
     path(route ='accounts/logout', 
         view=Logout.as_view(), 
         name='logout'),

    # CRUD #

     # Create User
     path(route ='accounts/register', 
          view=UserSignUpView.as_view(), 
          name='user-create'),
          
     # Create profile
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