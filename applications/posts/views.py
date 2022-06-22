""" DJANGO_APPS """
# HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

# Generics edit
from django.views.generic.edit import (
    
    CreateView,
    UpdateView,
    DeleteView,
)

#Login required
from django.contrib.auth.mixins import LoginRequiredMixin

""" THIRD_PARTY_APPS """
#...
""" LOCAL_APPS """
# Models
from applications.posts.models import Posts
from applications.users.models import Profile

# Forms
from applications.posts.forms import FormPost
# )

class HomeView(LoginRequiredMixin,TemplateView):
    """ Display a template """
    login_url = 'users:login'

    template_name = 'posts/home.html'

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Posts.objects.all()
        context['profile'] = Profile.objects.filter(user=request.user).first()
        return render(request, self.template_name, context)

class CreatePostView(CreateView, LoginRequiredMixin):
    """ Create posts """
    login_url = 'login'
    redirect_field_name = 'login'

    model = Posts
    template_name = 'posts/post_create.html'
    form_class = FormPost
    success_url = reverse_lazy('posts:home')

    def post(self, request):
        """ Create posts from logued in """
        form_post = self.form_class(request.POST, request.FILES)
        if form_post.is_valid():
            Posts.objects.create(
                profile_name = Profile.objects.filter(user=request.user).first(),
                description = form_post['description'].value(),
                post_image = form_post['post_image'].value(),
            )
        return HttpResponseRedirect(self.success_url)
