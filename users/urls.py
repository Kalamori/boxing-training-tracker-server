from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignUpView

urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view()),
]
