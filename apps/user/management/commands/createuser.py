from django.contrib.auth import get_user_model
from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)
from django.db import transaction

from apps.wallet.models import Wallet

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'username',
            type=str,
            help='Username',
        )

    def handle(self, *args, **kwargs) -> None:
        try:
            with transaction.atomic():
                user, created = User.objects.get_or_create(
                    username=kwargs['username'],
                    is_staff=False,
                    is_active=True,
                    is_superuser=False,
                )
                if created:
                    password = input('Password: ')
                    confirm_password = input('Confirm Password: ')
                    if (password == confirm_password):
                        user.set_password(raw_password=password)
                        user.save()
                        Wallet.objects.create(user=user)
                    else:
                        raise Exception('Passwords do not match')

        except Exception as e:
            command = __file__.split('/')[-1][:-3]
            raise CommandError(f'Failure in `{command}` command. '
                               f'Reason: {str(e)}.')
