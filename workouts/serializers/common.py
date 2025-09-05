from rest_framework.serializers import ModelSerializer
from ..models import Workout

class WorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "workout_type", "date", "duration", "notes"]

    def create(self, validated_data):
        request = self.context.get("request")
        return Workout.objects.create(owner=request.user, **validated_data)
