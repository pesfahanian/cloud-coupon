from django.urls import reverse

# from rest_framework import status

from apps.core.tests import TestCore


class TestCoupon(TestCore):
    coupon_route = reverse('coupon')

    def test_ok(self) -> None:
        pass
