from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Workout
from .serializers.common import WorkoutSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class WorkoutListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        if request.user.is_authenticated:
            workouts = Workout.objects.filter(owner=request.user).order_by('-date')
        else:
            workouts = Workout.objects.none()
        serialized_workouts = WorkoutSerializer(workouts, many=True)
        return Response(serialized_workouts.data)

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)

class WorkoutDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_workout(self, pk, user):
        try:
            workout = Workout.objects.get(pk=pk)
        except Workout.DoesNotExist:
            raise NotFound('Workout not found.')

        if workout.owner != user:
            raise PermissionDenied('You do not have permission to access this workout.')

        return workout

    def get(self, request, pk):
        workout = self.get_workout(pk)
        serialized_workout = WorkoutSerializer(workout)
        return Response(serialized_workout.data)

    def put(self, request, pk):
        workout = self.get_workout(pk, request.user)
        if workout.owner != request.user:
            raise PermissionDenied('You do not have permission to perform this action.')
        serialized_workout = WorkoutSerializer(workout, data=request.data)
        serialized_workout.is_valid(raise_exception=True)
        serialized_workout.save()
        return Response(serialized_workout.data)

    def delete(self, request, pk):
        workout = self.get_workout(pk)
        if workout.owner != request.user:
            raise PermissionDenied('You do not have permission to perform this action.')
        workout.delete()
        return Response(status=204)



    
