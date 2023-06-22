from django.urls import path, include

urlpatterns = [
    path(
        'user/',
        include('apps.user.api.urls'),
    ),
    path(
        'coupon/',
        include('apps.coupon.api.urls'),
    ),
    path(
        'wallet/',
        include('apps.wallet.api.urls'),
    ),
]
