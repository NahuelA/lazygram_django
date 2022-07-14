""" Urls from lazymovies """

from django.urls import path
from .views import SingleTemplateTv

urlpatterns = [

    path(
        route='',
        view= SingleTemplateTv.as_view(),
        name='lazymovies'
    )
]