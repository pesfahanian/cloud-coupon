from django.urls import reverse

from rest_framework import status

from apps.core.tests import TestCore


class TestCoupon(TestCore):
    coupon_route = reverse('coupon')

    def create_coupon(self) -> None:
        pass

    def test_ok(self) -> None:
        pass

    def test_invalid_user(self) -> None:
        response = self.client.get(
            path=self.coupon_route,
            headers=self.invalid_user_authorization_headers,
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEquals(
            response.data['results'],
            [],
        )
