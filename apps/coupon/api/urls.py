from django.urls import path

from apps.coupon.api import views

urlpatterns = [
    path(
        '',
        views.UserCouponListAPIView.as_view(),
        name='coupon',
    ),
]
