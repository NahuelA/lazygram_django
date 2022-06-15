""" Forms to submit posts """
from django.forms import (

    # Main class
    ModelForm,
    # Widgets
    FileInput,
    TextInput,
)

# Models
from .models import Posts

class FormPost(ModelForm):
    class Meta:
        model = Posts
        exclude = ('created', 'last_modified', 'profile_name')

        widgets = {

            'description': TextInput(attrs=
                                    {
                                    'class':'form-control',
                                    'required':False,
                                    'placeholder':'Description'
                                    }),

            'post_image': FileInput(attrs=
                                        {       
                                        'accept':(
                                            '.png',
                                            '.jpg',
                                            '.svg',
                                        ),
                                        'required':True,
                                        'multiple':True,
                                        'class':'form-control',
                                        })
        }
