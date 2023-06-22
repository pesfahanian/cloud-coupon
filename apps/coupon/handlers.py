from django.db import IntegrityError, transaction

from apps.coupon.models import Coupon, CouponType, UserCoupon

from apps.wallet.models import Wallet


def coupon_create_handler(**kwargs) -> None:
    Coupon.objects.create(**kwargs)


def user_coupon_create_handler(user_id: str, code: str) -> UserCoupon:
    try:
        wallet_obj = Wallet.objects.get(user_id=user_id)
        coupon_obj = Coupon.objects.get(code=code)

        if (coupon_obj.available_count >= 1):
            with transaction.atomic():
                user_coupon_obj = UserCoupon.objects.create(
                    user_id=user_id,
                    coupon=coupon_obj,
                )
                if (coupon_obj.type == CouponType.CREDIT):
                    user_coupon_obj.use()
                    wallet_obj.deposit(amount=coupon_obj.value)
                return user_coupon_obj
        else:
            raise Exception('Invalid coupon')

    except IntegrityError:
        raise Exception('Coupon is already used')

    except Wallet.DoesNotExist:
        raise Exception('Wallet does not exist')

    except Coupon.DoesNotExist:
        raise Exception('Coupon does not exist')
