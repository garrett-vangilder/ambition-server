from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, first_name, last_name, password):
        """Create a new user profile object"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create a new super user with given details"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Position(models.Model):
    name = models.CharField(max_length=255)
    name_abbreviated = models.CharField(max_length=255)


class Team(models.Model):
    name = models.CharField(max_length=255)
    name_abbreviated = models.CharField(max_length=255)


class Player(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile in our system."""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default=None, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, blank=True, null=True)
    salary = models.IntegerField(default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserProfileManager()
