from typing import Any

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import (
    TemporalModel,
    ToggleableModel,
    UUIDModel,
)

from apps.couponing.utils import generate_unique_code


class Server(models.IntegerChoices):
    USA = 0, _('USA')
    EU = 1, _('EU')
    UAE = 2, _('UAE')


class Coupon(UUIDModel, ToggleableModel, TemporalModel):

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    code = models.CharField(
        _('Code'),
        max_length=6,
        default=generate_unique_code,
        unique=True,
        blank=True,
    )
    value = models.FloatField(
        _('Value'),
        validators=[
            MinValueValidator(settings.MIN_COUPON_VALUE),
        ],
    )
    count = models.PositiveIntegerField(
        _('Count'),
        validators=[
            MinValueValidator(1),
        ],
    )

    server = models.SmallIntegerField(
        _('Server'),
        choices=Server.choices,
        null=True,
        blank=True,
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.initial_is_enabled = self.is_enabled

    def save(self, *args, **kwargs) -> None:
        if not self._state.adding:
            # * Children enable/disable logic
            if (self.is_enabled != self.initial_is_enabled):
                print(f'{Coupon.objects.filter(coupons__is_used=False) = }')
                UserCoupon.objects.filter(
                    coupon=self,
                    is_used=False,
                ).update(is_enabled=self.is_enabled)
        super().save(*args, **kwargs)

    @property
    def selected_count(self) -> int:
        return self.coupons.count()

    @property
    def used_count(self) -> int:
        return self.coupons.filter(is_used=True).count()

    @property
    def available_count(self) -> int:
        return self.count - self.selected_count

    def __str__(self) -> str:
        return self.code


class UserCoupon(UUIDModel, ToggleableModel, TemporalModel):

    class Meta:
        verbose_name = 'User Coupon'
        verbose_name_plural = 'User Coupons'

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='coupons',
    )
    coupon = models.ForeignKey(
        'couponing.Coupon',
        on_delete=models.CASCADE,
        related_name='coupons',
    )

    is_used = models.BooleanField(
        _('Is Used'),
        default=False,
    )

    def __str__(self) -> str:
        return f'{self.user}-{self.coupon}'
