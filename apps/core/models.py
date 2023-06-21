from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDModel(models.Model):

    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    def __str__(self) -> str:
        return str(self.id)


class TemporalModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True,
    )
