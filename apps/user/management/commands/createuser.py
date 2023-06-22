from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)

from apps.user.handlers import user_create_handler


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'username',
            type=str,
            help='Username',
        )

    def handle(self, *args, **kwargs) -> None:
        try:
            password = input('Password: ')
            confirm_password = input('Confirm Password: ')
            if (password == confirm_password):
                user_create_handler(
                    username=kwargs['username'],
                    password=password,
                )
            else:
                raise Exception('Passwords do not match')

        except Exception as e:
            command = __file__.split('/')[-1][:-3]
            raise CommandError(f'Failure in `{command}` command. '
                               f'Reason: {str(e)}.')
