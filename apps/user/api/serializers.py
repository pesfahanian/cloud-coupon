from collections import OrderedDict

from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: User, claims: dict = None) -> RefreshToken:
        token = super().get_token(user)
        return token

    def validate_username(self, username: str) -> str:
        return username.lower()

    def validate(self, attrs: OrderedDict) -> dict:
        data = super().validate(attrs)

        if not self.user.is_active:
            raise serializers.ValidationError(_('User is not active.'))

        refresh = super().get_token(user=self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
