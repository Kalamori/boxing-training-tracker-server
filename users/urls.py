from django.urls import path
from .views import SignUpView, MyTokenObtainPairView

urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', MyTokenObtainPairView.as_view()),
]
