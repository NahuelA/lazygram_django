""" View from users"""

""" DJANGO_APPS """
# HttpResponse
from django.shortcuts import (
    
    render,
    HttpResponseRedirect,
)
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


# Login account
def login_view(request, **kwargs):
    """ Login with any account """

    template_name = 'users/login.html'
    success_url = reverse('posts:home')
    permission_denied_message = 'Invalid account'
    form_class = FormUser

    if request.method == 'GET':
        # Render template from login
        return render(request, template_name, context={'form':form_class})
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
                            context={
                                    'form':form_class,
                                    'msg_error':[permission_denied_message, auth]
                                    }
                            )

# Logout account
@login_required(login_url='login')
def logout_view(request):
    """ Logout from account """
    success_url = reverse('users:login')
    logout(request)
    return HttpResponseRedirect(success_url)

# Create new user
class UserSignUpView(CreateView):
    """ Sign-up user from Copygram """

    model = User
    form_class = FormUser

    # reverse() generate a ImproperlyConfigured
    # and cause a circular import
    # Only in this view v:
    # I have no idea WHY xd
    # Because use reverse_lazy in success_url var
    success_url = reverse_lazy('users:profile-create') 
    template_name = 'users/users_create.html'

    def get_context_data(self, **kwargs):
        """ Return form to sign-up user """
        context = super().get_context_data(**kwargs)
        context['form_user'] = self.form_class
        return context
        
    def post(self, request, **kwargs):

        if request.method == 'POST':

            # Validate a password confirmation match
            # Push request post into variable
            form_user = self.form_class(request.POST)
            password_confirmation = request.POST.get('password-confirmation')
            password = request.POST.get('password')

            if form_user.is_valid():
                # Validate if username is already taken
                if self.form_class.clean_unique_user(form_user):
                    pass
                else:
                    # Validate if password == password-confirmation
                    if password == password_confirmation:
                        User.objects.create_user(
                                                form_user['username'].value(),
                                                form_user['email'].value(),
                                                form_user['password'].value(),
                                                first_name=form_user['first_name'].value(),
                                                last_name=form_user['last_name'].value(),
                                                )
                        # Login now and return the profile sign-up
                        auth = authenticate(
                                        request,
                                        username=form_user['username'].value(),
                                        password=form_user['password'].value(),
                                        )

                        login(request,auth)
                        return HttpResponseRedirect(redirect_to=self.success_url)
                    else:
                        # Invalid password confirmation
                        return render(request,
                                      self.template_name,
                                      context={
                                               'invalid_pass':'Invalid confirmation password',
                                               'form_user':self.form_class,
                                            })
            else:
                # Invalid save user
                errors = list(form_user._errors.values()) # Exception handling to django.forms.utils
                return render(request, self.template_name,
                              context={
                                       'error':errors,
                                       'form_user':self.form_class,
                                      })

        return super().post(request, **kwargs)

# Create profile
class ProfileSignUpView(LoginRequiredMixin, CreateView):
    """ Sign-up profile from Copygram """
    # Login required
    login_url = 'users:login'
    redirect_field_name = 'users:login'

    model = Profile
    form_class = FormProfile
    success_url = reverse_lazy('users:profile-view') 
    template_name = 'users/profile_create.html'
    template_redirect = 'users/profile_view.html'

    def post(self, request, **kwargs):
        """ Create profile from newly created user """
        # Adding post data in form class and saving in form_profile variable
        user = User.objects.filter(id=int(request.user.id)).first()
        form_profile = self.form_class(request.POST)
        if form_profile.is_valid():
            # Create profile to user
            Profile.objects.create(
                user = user,
                biography = request.POST.get('biography'),
                picture = request.FILES.get('picture'),
                date_of_birth = request.POST.get('date_of_birth'),
                website = request.POST.get('website'),
                phone_number = request.POST.get('phone_number'),
            )
            return HttpResponseRedirect(redirect_to=self.success_url)
        else:
            # Invalid save profile
            errors = list(form_profile._errors.values()) # Errors handled by django.forms.utils
            return render(request, self.template_name,
                            context={'error':errors,
                                    'form':self.form_class})

# Read profiles
class ProfileView(LoginRequiredMixin,ListView):
    """ List the information profile """
    # Login required
    login_url = 'users:login'
    redirect_field_name = 'users:login'

    model = Profile
    template_name = 'users/profile_view.html'

    def get(self, request, **kwargs):
        """ Display data for the authenticated user """
        context = {}
        # If user contains a profile
        profile_exist = Profile.exist_profile(self.model, request.user)
        if profile_exist:
            context['profile'] = self.model.objects.get(user=request.user)
            return render(request,
                            self.template_name,
                            context
                        )
        else:
            return render(request,
                            template_name=self.template_name,
                            context=
                                {
                                'does_not_profile':'Does not exist profile',
                                }
                        )

# Update profile
class ProfileUpdateView( UpdateView):
    """ Update profile from user
    
        Some fields is updates automatically:
            - last_login
            - date_joined (momently not alowed)
            - modified
            - is_active
    """
    # login required
    login_url = 'users:login'
    redirect_field_name = 'users:login'

    model = Profile
    template_name = 'users/profile_update.html'
    form_class = FormProfile
    success_url = reverse_lazy('users:profile-view')

    def get(self, request, **kwargs):
        """ Return template form update profile """
        if self.model.exist_profile(self.model, request.user):
            return super().get(request, **kwargs)
        else:
            return render(request,
                            template_name=self.template_name,
                            context=
                                {
                                'does_not_profile':'Does not exist profile',
                                }
                        )

    def post(self, request, **kwargs):

        # Get info to profile inputs
        filter_usr = Profile.objects.filter(pk=kwargs['pk']).first()
        form = FormProfile(data=request.POST, files=request.FILES, instance=filter_usr)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            errors = list(form._errors.values()) # Errors handled by django.forms.utils
            return render(request, self.template_name, context={'error':errors})