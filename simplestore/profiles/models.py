import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        superuser = self.create_user(email, password, **kwargs)
        superuser.is_admin = True
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save()

        return superuser


class Profile(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(blank=False, unique=True)
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Last Name"
    )
    slug = models.SlugField(blank=False)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    website = models.URLField(blank=True)
    about = models.TextField(blank=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return '{0} {1}'.format(self.name, self.surname)

    def __str__(self):
        return self.email
