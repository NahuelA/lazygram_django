""" Form to users login and edit profile """
from django.core.mail import send_mail
from django.forms import (

    # Main class
    ModelForm,
    # Widgets
    Textarea,
    NumberInput,
    FileInput,
    TextInput,
    PasswordInput,
    EmailInput,
    DateInput
)

# Validation
from django.core.exceptions import ValidationError

# Models
from .models import Profile
from django.contrib.auth.models import User

class FormUser(ModelForm):
    class Meta:
        model   = User
        exclude = [
                   'is_staff',
                   'is_active', 'date_joined',
                   'is_superuser','groups',
                   'user_permissions']
        widgets = {
            'username':TextInput(attrs={'required':True,
                                       
                                       'placeholder':'Username',
                                       'class':'form-control'}),

            'password':PasswordInput(attrs={'type':'password',
                                            'required':True,
                                            'placeholder':'Password',
                                            'class':'form-control'}),

            'email': EmailInput(attrs={'required':True,
                                       'placeholder':'youremail@email.com',
                                       'pattern':'.+@gmail\.com',
                                       'class':'form-control'}),

            'first_name':TextInput(attrs={
                                       'required':False,
                                       'placeholder':'First name',
                                       'class':'form-control'}),

            'last_name':TextInput(attrs={
                                       'required':False,
                                       'placeholder':'Last name',
                                       'class':'form-control'}),
    }

    # def send_email_verification(self, email):

    #     msg_email = 'Hi! Welcome to Copygram :D'
    #     subject = 'Successful registration!'
    #     # Send to mail if email exist

        
class FormProfile(ModelForm):
    class Meta:
        model   = Profile
        exclude = ['created','modified', 'age']
        widgets = {
            'biography':Textarea(attrs={'cols':10, 'rows':5,
                                        'required':False,
                                        'maxlength':20,
                                        'class':'form-control',
                                        'placeholder':'Biography',
                                    }),

            'picture':FileInput(attrs={'accept':(
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
            'date_of_birth':DateInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Date of birth',
                                        'type':'date'}),

            'website':TextInput(attrs={'placeholder':'Website',
                                       'required':False,
                                       'class':'form-control',
                                    }),

            'phone_number':NumberInput(attrs={'min':0,
                                              'required':False,
                                              'placeholder':'Phone number',
                                              'class':'form-control',}),
    }