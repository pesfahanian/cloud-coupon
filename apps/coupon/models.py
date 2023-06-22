from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TemporalModel, UUIDModel

from apps.coupon.utils import generate_unique_code


class Server(models.IntegerChoices):
    USA = 0, _('USA')
    EU = 1, _('EU')
    UAE = 2, _('UAE')


class CouponType(models.IntegerChoices):
    CREDIT = 0, _('Credit')
    DISCOUNT = 1, _('Discount')


class Coupon(UUIDModel, TemporalModel):

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
            MinValueValidator(0),
        ],
    )

    type = models.SmallIntegerField(
        _('Type'),
        choices=CouponType.choices,
    )
    server = models.SmallIntegerField(
        _('Server'),
        choices=Server.choices,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:
        if self._state.adding:
            if (self.type == CouponType.CREDIT) and self.server:
                raise Exception(
                    'Coupons with `Credit` type cannot have a `server` value')
        super().save(*args, **kwargs)

    @property
    def user_coupons_count(self) -> int:
        return self.coupons.count()

    @property
    def available_count(self) -> int:
        return self.count - self.user_coupons_count

    def __str__(self) -> str:
        return self.code


class UserCoupon(UUIDModel, TemporalModel):

    class Meta:
        verbose_name = 'User Coupon'
        verbose_name_plural = 'User Coupons'
        unique_together = (
            'user',
            'coupon',
        )

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='coupons',
    )
    coupon = models.ForeignKey(
        'coupon.Coupon',
        on_delete=models.CASCADE,
        related_name='coupons',
    )

    is_used = models.BooleanField(
        _('Is Used'),
        default=False,
    )

    def use(self) -> None:
        self.is_used = True
        self.save()

    def __str__(self) -> str:
        return f'{self.user}-{self.coupon}'
