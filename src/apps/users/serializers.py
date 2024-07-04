from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from .models import UserActivationToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + ('id', 'email',)
        read_only_fields = ('email',)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + ('id', 'email', 'password')

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error['non_field_errors']}
            )

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.perform_create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            # Making sure that user is inactive by default
            user.is_active = False
            user.save(update_fields=["is_active"])
        return user


class ActivationSerializer(serializers.Serializer):
    token = serializers.IntegerField()

    def validate_token(self, token):
        if UserActivationToken.objects.filter(token=token).exists():
            self.user = UserActivationToken.objects.get(token=token).user
            return token
        else:
            raise serializers.ValidationError(
                {'message': "Invalid token"}
            )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.user.is_active:
            return attrs
        raise PermissionDenied(
            {'message': 'Stale Token'}
        )
