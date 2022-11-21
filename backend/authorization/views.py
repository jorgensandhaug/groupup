from core.models import User
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.views import View
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from rest_framework.response import Response


class LoginView(ObtainAuthToken):
    """
    Loginview for obtaining token
    """

    def post(self, request, *args, **kwargs):
        try:
            user = authenticate(
                request=request,
                username=request.data["username"],
                password=request.data["password"],
            )
            if not user:
                return Response(status=400)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "id": user.id,
                    "username": user.username,
                    "birthdate": user.birthdate,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            )
        except:
            return Response(status=400)


class ValidateTokenView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=200)


class RegisterView(CreateAPIView):
    """
    Create a view that takes a POST request
    with a username, email and password, and creates a user with that info
    """

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        token, created = Token.objects.get_or_create(user_id=response.data["id"])
        response.data["token"] = str(token)
        del response.data["password"]
        return response
