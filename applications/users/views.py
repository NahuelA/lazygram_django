""" View from users"""

""" DJANGO_APPS """
# HttpResponse
import json
import profile
from xml.dom import VALIDATION_ERR
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Generics edit
from django.views.generic.edit import (
    
    CreateView,
    UpdateView,
    DeleteView,
)

# List the views
from django.views.generic.list import ListView

# Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (

    # views, ***REVISE***
    authenticate,
    login,
    logout,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.admin CHANGE PASSWORD
# from django.contrib.auth.hashers

# Exceptions
from django.db.utils import IntegrityError

# Forms
from applications.users.forms import (

    FormUser,
    FormProfile,
)

""" THIRD_PARTY_APPS """
# ...
""" LOCAL_APPS """

# Models
from applications.users.models import Profile
from django.contrib.auth.models import User

# Login function
def login_view(request, **kwargs):
    """ Login with any account """

    template_name = 'users/login.html'
    success_url = reverse('home')
    permission_denied_message = 'Invalid account'
    form_class = FormUser

    if request.method == 'GET':
        # Render template from login
        return render(request, template_name, context={'form':form_class})
    try:
        if request.method == 'POST':
            # Get post
            username = request.POST['username']
            password = request.POST['password']

            # Auth
            auth = authenticate(request, username=username, password=password)

            # If user not found, user = None
            if auth != None:

                # Login and redirect
                login(request, auth)
                return HttpResponseRedirect(redirect_to=success_url)

            else:
                # If user is not found
                return render (request, template_name,
                                context={'form':form_class,
                                        'msg_error':[permission_denied_message, auth]}
                            )
    except Exception as err: # Fix Exception
        return err

# Logout function
@login_required(login_url='login')
def logout_view(request, **kwargs):
    """ Logout from account """

    success_url = reverse('login')
    logout(request)
    return HttpResponseRedirect(success_url)

# Create and View
class UserSignUpView(CreateView):
    """ Sign-up user from Copygram """

    model = User
    form_class = FormUser

    # reverse() generate a ImproperlyConfigured
    # and cause a circular import
    # Only in this view v:
    # I have no idea WHY xd
    # Because use reverse_lazy in success_url var
    success_url = reverse_lazy('profile-sign-up') 
    template_name = 'users/form_users.html'

    def get_context_data(self, **kwargs):
        """ Return form and all context """

        context = super().get_context_data(**kwargs)
        # Form sign-up user
        context['form_user'] = self.form_class
        return context
        
    def post(self, request, **kwargs):

        if request.method == 'POST':

            # Get info to User inputs
            username = request.POST['username']
            password = request.POST['password']
            pass_confirmation = request.POST.get('password-confirmation')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            if pass_confirmation == password:
                
                # If the username found, not create user
                auth = authenticate(request, username=username, password=password)
                data_user ={
                      'username':username,
                      'password':password,
                      'email':email,
                      'first_name':first_name,
                      'last_name':last_name
                    }

                form_user = self.form_class(data_user)

                if auth == None:
                    if form_user.is_valid():
                        # Sign-up user!
                        User.objects.create_user(form_user['username'].value(),
                                                 form_user['email'].value(),
                                                 form_user['password'].value(),
                                                 first_name=form_user['first_name'].value(),
                                                 last_name=form_user['last_name'].value(),
                                                )
                        # Login now
                        auth = authenticate(request,
                                            username=form_user['username'].value(),
                                            password=form_user['password'].value()
                                        )
                        if auth != None:
                            login(request,auth)
                            return HttpResponseRedirect(redirect_to=self.success_url)
                    else:
                        # Invalid save user
                        errors = list(form_user._errors.values()) # Exception handling to django.forms.utils
                        return render(request, self.template_name,
                                        context={'error':errors,
                                                 'form_user':self.form_class,
                                                })
                else:
                    # Error username invalid
                    return render(request, self.template_name,
                                        context={'error':'This name is already use in or email invalid',
                                                 'form_user':self.form_class,
                                                })
            else:
                # Error password auth invalid
                return render(request, self.template_name,
                                        context={'error':'Password authentication invalid',
                                                 'form_user':self.form_class,
                                                })
        return super().post(request, **kwargs)


class ProfileSignUpView(LoginRequiredMixin, CreateView):
    """ Sign-up profile from Copygram """
    # Login required
    login_url = 'login'
    redirect_field_name = 'login'

    model = Profile
    form_class = FormProfile
    success_url = reverse_lazy('profile') 
    template_name = 'users/form_profile.html'
    template_redirect = 'users/profile.html'

    def get_context_data(self, **kwargs):
        """ Return form and all context """
        context = super().get_context_data(**kwargs)
        # Form sign-up Profile
        context['form_profile'] = self.form_class
        return context
    
    def post(self, request, **kwargs):
        """ Create profile information from newly created user """
        if request.method == 'POST':

            # User for OneToOneField
            user = User.objects.get(username=str(request.user))
            # Get info to profile inputs
            data_profile = {
                    'user':user,
                    'biography':    request.POST.get('biography'),
                    'picture':      request.POST.get('picture'),
                    'date_of_birth':request.POST.get('date_of_birth'),
                    'website':      request.POST.get('website'),
                    'phone_number': request.POST.get('phone_number'),
                    }

            # Adding post data in form class and saving in form_profile variable
            form_profile = self.form_class(data_profile)
            if form_profile.is_valid():
                # Create profile for user
                form_profile.save()
                return HttpResponseRedirect(redirect_to=self.success_url)
            else:
                # Invalid save profile
                errors = list(form_profile._errors.values()) # Errors handled by django.forms.utils
                return render(request, self.template_name,
                                context={'error':errors,
                                         'form_profile':self.form_class})
        return super().post(request, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Update profile from user
    
        Some fields is updates automatically:
            - last_login
            - date_joined (momently not alowed)
            - modified
            - is_active
    """
    # Login required
    login_url = 'login'
    redirect_field_name = 'login'

    model = Profile
    template_name = 'users/profile_edit.html'
    form_class = FormProfile
    # success_url

class ProfileView(LoginRequiredMixin,ListView):
    """ List the information profile """
    # Login required
    login_url = 'sign-up'
    redirect_field_name = 'sign-up'

    model = Profile
    template_name = 'users/profile.html'

    def get(self, request, **kwargs):
        """ Display data for the authenticated user """
        context = {}
        try:
            # If user contains a profile
            if Profile.exist_profile(self.model, request.user):
                context['data_profile'] = self.model.objects.get(user=request.user)
                context['data_user'] = User.objects.get(username=request.user)
                return render(request,
                              self.template_name,
                              context)
            else:
                return render(request,
                              template_name=self.template_name,
                              context={'error':'Does not exist profile'})
        except Exception as exc:
            # Fix and handled error
            return render(request,
                          self.template_name,
                          context={'exception':exc})