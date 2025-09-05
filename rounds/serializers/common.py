from rest_framework.serializers import ModelSerializer
from ..models import Round

class RoundSerializer(ModelSerializer):
    class Meta:
        model = Round
        fields = ['id', 'workout', 'owner', 'round_number', 'time', 'intensity', 'notes']
        read_only_fields = ['owner']
        
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)