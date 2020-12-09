from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from blog.authentication.models import CustomUser


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, min_length=6)
    username = serializers.CharField(required=True, min_length=4)
    password = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "password",
            "email",
            "username",
            "first_name",
            "last_name",
            "url",
            "date_of_birth",
        ]

    def create(self, validated_data):
        email = validated_data["email"]
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(_("The email is already in use"))
        return CustomUser.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "url",
            "date_of_birth",
        ]
        read_only_fields = ["email", "username"]
