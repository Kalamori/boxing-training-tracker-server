from django.urls import path
from rounds.views import RoundListView, RoundDetailView

urlpatterns = [
    path('', RoundListView.as_view(), name='round-list'),
    path('<int:pk>/', RoundDetailView.as_view(), name='round-detail'),
]
