from .serializers.token import TokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.common import AuthSerializer
from .serializers.token import TokenSerializer

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer_user = AuthSerializer(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        serializer_user.save()

        user = User.objects.get(pk=serializer_user.data['id'])
        refresh = TokenSerializer.get_token(user)
        return Response({'access': str(refresh.access_token), 'user': str(user.username)}, status=201)
