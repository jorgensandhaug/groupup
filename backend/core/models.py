from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    # Create a new user profile
    def create_user(self, email, username, password):

        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    # Create a new superuser profile
    def create_superuser(self, email, username, password):

        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


# Database model for users in the system
class User(AbstractBaseUser, PermissionsMixin):

    # Fields for the user model
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="")
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    is_staff = models.BooleanField(default=False, verbose_name="staff status")
    birthdate = models.DateField(null=True, blank=True)

    # avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    # interestGroups = models.ManyToManyField(InterestGroup, blank=True)

    # Usermanager for creating users
    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
