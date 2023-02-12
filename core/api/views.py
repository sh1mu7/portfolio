from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from ..models import User, UserWebsite
from ..utils import auth_utils
from rest_framework import viewsets


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


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = UserWebsite.objects.all()
    serializer_class = serializers.WebsiteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        user = request.user
        user_website_info = UserWebsite.objects.filter(author=user)
        if user_website_info:
            return Response({"error": "You already created website information."})
        else:
            return super().create(request, *args, **kwargs)
