from django.urls import reverse

from rest_framework import status

from apps.core.tests import TestCore


class TestWallet(TestCore):
    wallet_route = reverse('wallet')

    def test_ok(self) -> None:
        response = self.client.get(
            path=self.wallet_route,
            headers=self.valid_user_authorization_headers,
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertIn(
            'balance',
            response.data,
        )

    def test_invalid(self) -> None:
        response = self.client.get(
            path=self.wallet_route,
            headers=self.invalid_user_authorization_headers,
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )
