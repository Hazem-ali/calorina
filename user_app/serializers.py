from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_confirm",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        
        validated_data.pop('password_confirm')
        
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user

