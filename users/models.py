from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def _create_user(self, username, phone, password, **extra_fields):
        user = self.model(
            username=username,
            phone=phone,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone, password):
        return self._create_user(username, phone, password)

    def create_superuser(self, username, phone, password):
        return self._create_user(
            username, phone, password, is_staff=True, is_superuser=True
        )


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'phone'.split()
    objects = UserManager()

    def __str__(self):
        return self.username
