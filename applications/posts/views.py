""" DJANGO_APPS """
# HttpResponse
from django.shortcuts import render

from django.views.generic.base import TemplateView

# Generics edit
from django.views.generic.edit import (
    
    CreateView,
    UpdateView,
    DeleteView,
)

#Login required
from django.contrib.auth.mixins import LoginRequiredMixin

""" THIRD_PARTY_APPS """
from datetime import datetime
#...
""" LOCAL_APPS """
# Models
from applications.posts import models
# )

profiles = {
    '1':{
        'name':'Ferreyra Gonzalo',
        'website':'https://translate.google.com/?hl=es&sl=en&tl=es&op=translate',
        'username':'Gonzi el piola',
        'picture':'https://img.freepik.com/foto-gratis/retrato-joven-sonriente-gafas_171337-4842.jpg?t=st=1651905672~exp=1651906272~hmac=19cd375bffbbc4f423827813a1099061440d3c798fabb49448c3f53a2799f73a&w=740',
        'description':'I have hungry and i am tired',
        'last_modified':datetime.now()
    },
    '2':{

        'name':'Carrefour Marcelo',
        'website':'https://translate.google.com/?hl=es&sl=en&tl=es&op=translate',
        'username':'Flamenco',
        'picture':'https://img.freepik.com/foto-gratis/retrato-joven-sonriente-senalando-dedo_171337-1619.jpg?t=st=1651905672~exp=1651906272~hmac=83f227b5695906a6581c5a8bc34cb5c144d4cd7ee2f9d963eea8eac65de25c52&w=740',
        'description':'I have hungry and i am tired',
        'last_modified':datetime.now()
    },
    '3':{

        'name':'Blanco Ignacio',
        'website':'https://translate.google.com/?hl=es&sl=en&tl=es&op=translate',
        'username':'Gonzales',
        'picture':'https://img.freepik.com/foto-gratis/hombre-computadora-portatil-estudiante-computadora-aislado-tenencia-persona_488220-37851.jpg?w=740',
        'description':'I am hungry and i am tired',
        'last_modified':datetime.now()
    }
}

class HomeView(LoginRequiredMixin,TemplateView):
    """ Display a template """
    login_url = 'login'
    redirect_field_name = 'login'

    template_name = 'posts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = profiles

        return context