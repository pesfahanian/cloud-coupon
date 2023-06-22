from django.urls import reverse

from rest_framework import status

from apps.core.tests import TestCore

from apps.coupon.models import Coupon, CouponType, Server


class TestCoupon(TestCore):
    coupon_route = reverse('coupon')

    @property
    def coupon(self) -> dict:
        return {
            'credit': Coupon.objects.get(code='ABC123'),
            'discount': Coupon.objects.get(code='XYZ789'),
        }

    def create_user_credit_coupon(self) -> None:
        data = {
            'code': self.coupon['credit'].code,
        }
        return self.client.post(
            path=self.coupon_route,
            data=data,
            headers=self.valid_user_authorization_headers,
            format='json',
        )

    def create_user_discount_coupon(self) -> None:
        data = {
            'code': self.coupon['discount'].code,
        }
        return self.client.post(
            path=self.coupon_route,
            data=data,
            headers=self.valid_user_authorization_headers,
            format='json',
        )

    def test_filters(self) -> None:
        self.create_user_credit_coupon()
        self.create_user_discount_coupon()

        valid_filter_data = [
            {
                'type': CouponType.CREDIT,
            },
            {
                'type': CouponType.DISCOUNT,
            },
            {
                'server': Server.USA,
            },
            {
                'is_used': True,
            },
            {
                'is_used': False,
            },
        ]

        invalid_filter_data = [
            {
                'type': self.invalid_coupon_type,
            },
            {
                'server': self.invalid_server,
            },
        ]

        for data in valid_filter_data:
            response = self.client.get(
                path=self.coupon_route,
                data=data,
                headers=self.valid_user_authorization_headers,
            )
            self.assertEquals(
                response.status_code,
                status.HTTP_200_OK,
            )
            self.assertNotEqual(
                response.data['results'],
                [],
            )

        for data in invalid_filter_data:
            response = self.client.get(
                path=self.coupon_route,
                data=data,
                headers=self.valid_user_authorization_headers,
            )
            self.assertEquals(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
            )

    def test_create_user_credit_coupon(self) -> None:
        response = self.create_user_credit_coupon()
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEquals(
            self.valid_user_wallet.balance,
            self.coupon['credit'].value,
        )

    def test_create_user_discount_coupon(self) -> None:
        response = self.create_user_discount_coupon()
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEquals(
            self.valid_user_wallet.balance,
            0,
        )

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

    def test_coupon_is_already_used(self) -> None:
        self.create_user_discount_coupon()
        response = self.create_user_discount_coupon()
        print(f'{response.json() = }')
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_coupon_does_not_exist(self) -> None:
        data = {
            'code': self.invalid_code,
        }
        response = self.client.post(
            path=self.coupon_route,
            data=data,
            headers=self.valid_user_authorization_headers,
            format='json',
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_invalid_coupon(self) -> None:
        self.create_user_credit_coupon()
        data = {
            'code': self.coupon['credit'].code,
        }
        response = self.client.post(
            path=self.coupon_route,
            data=data,
            headers=self._valid_user_authorization_headers,
            format='json',
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
