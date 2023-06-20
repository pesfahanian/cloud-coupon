from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **kwargs) -> None:
        try:
            pass

        except Exception as e:
            command = __file__.split('/')[-1][:-3]
            raise CommandError(f'Failure in `{command}` command. '
                               f'Reason: {str(e)}.')
