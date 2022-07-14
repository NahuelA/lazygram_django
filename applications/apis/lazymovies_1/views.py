""" Lazymovies api view """

from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, get_user
#Login required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User


class SingleTemplateTv(TemplateView):
    """ Sigle page app for lazymovies """
    login_url = reverse_lazy('users:login')
    template_name = 'lazymovies/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return super().get(request)
        else:
            return HttpResponseRedirect(self.login_url)