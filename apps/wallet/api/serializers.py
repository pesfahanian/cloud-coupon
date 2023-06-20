from django.utils.translation import gettext_lazy as _

from apps.core.api.serializers import TemporalModelSerializer

from apps.wallet.models import Wallet


class WalletSerializer(TemporalModelSerializer):

    class Meta:
        model = Wallet
        fields = (
            'id',
            'balance',
        ) + TemporalModelSerializer.Meta.fields
