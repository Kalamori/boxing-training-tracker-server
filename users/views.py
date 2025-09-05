from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import AuthSerializer
from .models import User

from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class SignUpView(APIView):
    def post(self, request):
        serializer_user = AuthSerializer(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        serializer_user.save()

        user = User.objects.get(pk=serializer_user.data['id'])
        refresh = RefreshToken.for_user(user)
        return Response({'access': str(refresh.access_token)}, status=201)
