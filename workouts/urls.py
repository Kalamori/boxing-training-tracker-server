from django.urls import path
from workouts.views import WorkoutListView, WorkoutDetailView

urlpatterns = [
    path('', WorkoutListView.as_view(), name='workout-list'),
    path('<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),
]
