from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Round
from .serializers.common import RoundSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RoundListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = RoundSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)

    def get(self, request):
        rounds = Round.objects.all()
        serialized_rounds = RoundSerializer(rounds, many=True)
        return Response(serialized_rounds.data)

class RoundDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_round(self, pk):
        try:
            return Round.objects.get(pk=pk)
        except Round.DoesNotExist:
            raise NotFound('Round not found.')

    def put(self, request, pk):
        round = self.get_round(pk)
        if round.owner != request.user:
            raise PermissionDenied('You do not have permission to edit this round.')
        serialized_round = RoundSerializer(round, data=request.data)
        serialized_round.is_valid(raise_exception=True)
        serialized_round.save()
        return Response(serialized_round.data)

    def delete(self, request, pk):
        round = self.get_round(pk)
        if round.owner != request.user:
            raise PermissionDenied('You do not have permission to delete this round.')
        round.delete()
        return Response(status=204)
    
