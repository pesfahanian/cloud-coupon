from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.core.models import UUIDModel, TemporalModel

from apps.user.managers import CustomUserManager, ActiveUserManager


class User(AbstractUser, UUIDModel, TemporalModel):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    objects = CustomUserManager()
    active_objects = ActiveUserManager()

    first_name = None
    last_name = None
    date_joined = None

    def __str__(self) -> str:
        return self.username
