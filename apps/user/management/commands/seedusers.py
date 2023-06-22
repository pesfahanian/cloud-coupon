from django.core.management.base import BaseCommand, CommandError

from apps.user.handlers import user_create_handler


class Command(BaseCommand):

    def handle(self, *args, **kwargs) -> None:
        try:
            for username in [
                    'alice',
                    'bob',
                    'charlie',
            ]:
                user_create_handler(
                    username=username,
                    password='1234',
                )

        except Exception as e:
            command = __file__.split('/')[-1][:-3]
            raise CommandError(f'Failure in `{command}` command. '
                               f'Reason: {str(e)}.')
