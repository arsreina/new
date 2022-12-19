from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import AppUser
from phonenumber_field.modelfields import PhoneNumberField


class RegistrationSerializer(serializers.ModelSerializer):
    password_ver = serializers.CharField(min_length=8, max_length=100,
                                         write_only=True, style={'input_type': 'password'})
    password = serializers.CharField(min_length=8, max_length=100,
                                     write_only=True, style={'input_type': 'password'})

    class Meta:
        model = AppUser
        fields = 'username phone password password_ver'.split()
        extra_fields = {'password_ver': {'write_only': True}}

    def save(self):
        username = self.validated_data.get('username')
        password = self.validated_data.get('password')
        password_ver = self.validated_data.get('password_ver')
        if not username.isalnum():
            raise ValidationError('use only letters and numbers')
        if not password == password_ver:
            raise ValidationError('passwords do not match')
        user = AppUser.objects.create_user(username, self.validated_data.get('phone'), password)
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = AppUser

    phone = PhoneNumberField()
    password = serializers.CharField(min_length=8, max_length=100)


class AppUserSerializer(serializers.Serializer):
    class Meta:
        model = AppUser
        fields = 'username phone password'.split()

    username = serializers.CharField(min_length=3, max_length=100)
    phone = PhoneNumberField()
    password = serializers.CharField(min_length=8, max_length=100, write_only=True)


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = AppUser
        fields = 'username phone email address image'.split()

    email = serializers.EmailField()
    address = serializers.CharField(max_length=100, required=True)
    image = serializers.ImageField(required=False)
