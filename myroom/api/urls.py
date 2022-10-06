from api.views import BlacklistTokenUpdateView
from django.views.generic import base

from account.views import UserViewSet
from vendor.views import VendorViewSet
from review.views import ReviewViewSet
from booking.views import BookedViewSet
from booking.views import PaymentViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()



urlpatterns=[
    
    
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/',BlacklistTokenUpdateView.as_view(),name="blacklist")
]

router.register(r'user', UserViewSet,basename='user')
router.register(r'room',VendorViewSet)
router.register(r'review',ReviewViewSet)
router.register(r'booking',BookedViewSet)
urlpatterns +=router.urls
