from django.contrib.auth import get_user_model
from django.db import transaction

from apps.wallet.models import Wallet

User = get_user_model()


def user_create_handler(username: str, password: str) -> None:
    with transaction.atomic():
        user, created = User.objects.get_or_create(
            username=username,
            is_staff=False,
            is_active=True,
            is_superuser=False,
        )
        if created:
            user.set_password(raw_password=password)
            user.save()
            Wallet.objects.create(user=user)
        else:
            raise Exception('User already exists')
