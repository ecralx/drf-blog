from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password", "username"]

    objects = CustomUserManager()

    url = models.URLField(max_length=100, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
