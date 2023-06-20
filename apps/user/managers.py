from django.contrib.auth.models import UserManager
from django.db.models.query import QuerySet


class CustomUserManager(UserManager):
    pass


class ActiveUserManager(UserManager):

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_active=True, )
