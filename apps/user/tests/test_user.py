import jwt

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status

from apps.core.tests import TestCore


class TestLogin(TestCore):
    login_route = 'login'

    def test_ok(self) -> None:
        data = {
            'username': self.valid_username,
            'password': self.valid_password,
        }
        response = self.client.post(
            path=reverse(self.login_route),
            data=data,
            format='json',
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertIn(
            'access',
            response.data,
        )
        self.assertIn(
            'refresh',
            response.data,
        )

    def test_invalid(self) -> None:
        response = self.invalid_login()
        self.assertEquals(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )


class TestToken(TestCore):
    token_route = 'token'

    def test_happy(self) -> None:
        data = {
            'refresh': self.get_token()['refresh'],
        }

        response = self.client.post(
            path=reverse(self.token_route),
            data=data,
            format='json',
        )

        user_id = jwt.decode(
            response.json()['access'],
            options={'verify_signature': False},
        )['user_id']

        User = get_user_model()
        user = User.objects.get(username=self.valid_username)

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEquals(
            str(user.id),
            user_id,
        )
