from django.urls import path
from rest_framework.authtoken import views as auth_views
from .views import RegisterView, LoginView, ValidateTokenView

# The `urlpatterns` variable is a list of all the URLs that can be requested from the server.
#
# The `path` function is a function that takes two arguments:
#
# 1. The URL that you want to add to the list of URLs that can be requested from the server.
#
# 2. The view function that you want to run when the URL is requested.
#
# The `auth_views` module is a module that Django provides that contains a number of pre-built view
# functions.
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("validateToken/", ValidateTokenView.as_view(), name="validateToken"),
    path("register/", RegisterView.as_view(), name="register"),
]
