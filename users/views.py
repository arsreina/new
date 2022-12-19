from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import LoginSerializer, RegistrationSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from .models import AppUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffUser


class RegistrationView(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        print(request.user)
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(phone=serializer.validated_data.get('phone'),
                            password=serializer.validated_data.get('password'))
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key},
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProfileViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [IsStaffUser]
