from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from ..models import User
from ..utils import auth_utils


class LoginAPI(APIView):
    permission_classes = [AllowAny, ]

    @extend_schema(
        request=serializers.LoginSerializer,
        responses={200: serializers.LoginSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=str(serializer.validated_data['email']))
            auth_utils.get_user_by_email(user)
            token, created = auth_utils.regenerate_token(user=user)
            data = {'email': 'Login Successfully', 'token': token.key}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)
