import random

from django.core.management.base import BaseCommand, CommandError

from apps.coupon.handlers import coupon_create_handler
from apps.coupon.models import CouponType, Server

COUNT = 10


class Command(BaseCommand):

    def handle(self, *args, **kwargs) -> None:
        try:
            for _ in range(COUNT):
                kwargs = {
                    'value': random.randint(5, 100),
                    'count': random.randint(1, 100),
                }
                kwargs['type'] = random.choice(CouponType.choices)[0]
                if (kwargs['type'] == CouponType.DISCOUNT):
                    kwargs['server'] = random.choice(Server.choices)[0]

                coupon_create_handler(**kwargs)

        except Exception as e:
            command = __file__.split('/')[-1][:-3]
            raise CommandError(f'Failure in `{command}` command. '
                               f'Reason: {str(e)}.')
