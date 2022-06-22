""" Form to users login and edit profile """
# All forms
from django import forms

# Validation
from django.core.exceptions import ValidationError
# from django.core.validators

# Models
from .models import Profile
from django.contrib.auth.models import User

class FormUser(forms.ModelForm):
    class Meta:
        model   = User
        exclude = [
                   'is_staff',
                   'is_active', 'date_joined',
                   'is_superuser','groups',
                   'user_permissions']
        widgets = {
            'username':forms.TextInput(attrs={'required':True,
                                       
                                       'placeholder':'Username',
                                       'class':'form-control'}),

            'password':forms.PasswordInput(attrs={'type':'password',
                                            'required':True,
                                            'placeholder':'Password',
                                            'class':'form-control'}),

            'email': forms.EmailInput(attrs={'required':True,
                                       'placeholder':'youremail@email.com',
                                       'pattern':'.+@gmail\.com',
                                       'class':'form-control'}),

            'first_name':forms.TextInput(attrs={
                                       'required':False,
                                       'placeholder':'First name',
                                       'class':'form-control'}),

            'last_name':forms.TextInput(attrs={
                                       'required':False,
                                       'placeholder':'Last name',
                                       'class':'form-control'}),
    }

    def clean_unique_user(self):
        
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already in use', code='username_invalid')
        else:
            return False

class FormLogin(forms.Form):

    username = forms.CharField(
                                max_length=150,
                                widget=
                                       forms.TextInput(attrs={
                                       'required':True,
                                       'autofocus':True,
                                       'placeholder':'Username',
                                       'class':'form-control'})
                                )
    password = forms.CharField(
                                widget=
                                    forms.PasswordInput(attrs={
                                    'type':'password',
                                    'autocomplete':'current-password',
                                    'required':True,
                                    'placeholder':'Password',
                                    'class':'form-control'})
                            )

class FormProfile(forms.ModelForm):
    class Meta:
        model   = Profile
        exclude = ['created','modified', 'age', 'user']
        widgets = {
            'biography':forms.Textarea(attrs={'cols':10, 'rows':5,
                                        'required':False,
                                        'maxlength':20,
                                        'class':'form-control',
                                        'placeholder':'Biography',
                                    }),

            'picture':forms.FileInput(attrs={'accept':(
                                                '.png',
                                                '.jpg',
                                                '.svg',
                                                ),
                                        'required':False,
                                        'multiple':False,
                                        'capture':'environment',
                                        'class':'form-control',
                                        'placeholder':'Picture'
                                        }),
            'date_of_birth':forms.DateInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Date of birth',
                                        'type':'date'}),

            'website':forms.TextInput(attrs={'placeholder':'Website',
                                       'required':False,
                                       'class':'form-control',
                                    }),

            'phone_number':forms.NumberInput(attrs={'min':0,
                                              'required':False,
                                              'placeholder':'Phone number',
                                              'class':'form-control',}),
    }
    