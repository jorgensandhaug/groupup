"""backend URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from groupApp import views as groupAppViews

# The `urlpatterns` variable is a list of all the URLs that can be requested from the server.
#
# The `path` function is a function that takes two arguments:
#
# 1. The URL that you want to add to the list of URLs that can be requested from the server.
#
# 2. The view function that you want to run when the URL is requested.
#
# The first path function call is the admin page of the site.
# The second path function call is the api/ url, which is where all of the api calls will be routed.
# The third path function call is the auth/ url, which is where all of the authentication calls will
router = routers.DefaultRouter()
router.register(r"groups", groupAppViews.InterestGroupViewSet)
router.register(r"interests", groupAppViews.InterestViewSet)
router.register(r"groupups", groupAppViews.GroupUpViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("auth/", include("authorization.urls")),
]
