import jwt

from django.urls import reverse

from rest_framework import status

from apps.core.tests import TestCore


class TestLogin(TestCore):
    login_route = reverse('login')

    def test_ok(self) -> None:
        response = self.get_token()
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

    def test_invalid_data(self) -> None:
        data = {
            'username': self.invalid_username,
            'password': self.invalid_password,
        }
        response = self.client.post(
            path=self.login_route,
            data=data,
            format='json',
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )


class TestToken(TestCore):
    token_route = reverse('token')

    def test_ok(self) -> None:
        data = {
            'refresh': self.get_token().json()['refresh'],
        }

        response = self.client.post(
            path=self.token_route,
            data=data,
            format='json',
        )

        user_id = jwt.decode(
            response.json()['access'],
            options={'verify_signature': False},
        )['user_id']

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEquals(
            str(self.valid_user.id),
            user_id,
        )


class TestUser(TestCore):
    user_route = reverse('user')

    def test_ok(self) -> None:
        response = self.client.get(
            path=self.user_route,
            headers=self.valid_user_authorization_headers,
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertIn(
            'id',
            response.data,
        )
        self.assertIn(
            'username',
            response.data,
        )

    def test_invalid_user(self) -> None:
        response = self.client.get(
            path=self.user_route,
            headers=self.invalid_user_authorization_headers,
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )
