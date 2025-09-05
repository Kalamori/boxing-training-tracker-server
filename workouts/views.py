from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Workout
from .serializers.common import WorkoutSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class WorkoutListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        workouts = Workout.objects.all()
        serialized_workouts = WorkoutSerializer(workouts, many=True)
        return Response(serialized_workouts.data)

    def post(self, request):
        serialized_workouts = WorkoutSerializer(data=request.data, context={'request': request})
        serialized_workouts.is_valid(raise_exception=True)
        serialized_workouts.save()
        return Response(serialized_workouts.data, status=201)

class WorkoutDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_workout(self, pk):
        try:
            return Workout.objects.get(pk=pk)
        except Workout.DoesNotExist:
            raise NotFound('Workout not found.')

    def get(self, request, pk):
        workout = self.get_workout(pk)
        serialized_workout = WorkoutSerializer(workout)
        return Response(serialized_workout.data)

    def put(self, request, pk):
        workout = self.get_workout(pk)
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



    
