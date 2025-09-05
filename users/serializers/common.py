from rest_framework import serializers
from ..models import User

class AuthSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "bio", "password", "password_confirmation"]

    def validate(self, data):
        if "email.com" in data["email"].lower():
            raise serializers.ValidationError(
                {"email": "We do not accept email addresses from 'email.com'. Please use a different provider."}
            )
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError(
                {"password_confirmation": "Passwords do not match."}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        user = User.objects.create_user(**validated_data)
        return user