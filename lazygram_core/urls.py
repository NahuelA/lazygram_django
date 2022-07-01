"""copygram_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# To load media data into templates
from django.conf.urls.static import static
# To read MEDIA_URL const from settings module
from django.conf import settings

# Paths
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    # Local apps
    path(
        route='',
        view=include(('applications.posts.urls', 'posts'),
        namespace='posts')
    ),
    path(
        route='users/',
        view=include(('applications.users.urls','users'),
        namespace='users')
    ),

    # Api lazymovies
    path(
        route='lazymovies/',
        view=include('applications.apis.lazymovies.urls'),
        name='lazymoviews'
    )
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
