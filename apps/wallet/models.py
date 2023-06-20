import logging

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import (
    TemporalModel,
    ToggleableModel,
    UUIDModel,
)

logger = logging.getLogger('django')


class Wallet(UUIDModel, ToggleableModel, TemporalModel):

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    user = models.OneToOneField(
        'user.User',
        on_delete=models.CASCADE,
        related_name='wallet',
    )

    balance = models.FloatField(
        _('Balance'),
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )

    def deposit(self, amount: float) -> None:
        logger.info(f'Depositing `{amount}` to user `{self.user}` wallet.')
        self.balance += amount
        self.save()

    def __str__(self) -> str:
        return f'{self.user}-wallet'
