from django.urls import path

from apps.coupon.api import views

urlpatterns = [
    path(
        '',
        views.CouponListAPIView.as_view(),
    ),
]
