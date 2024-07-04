from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer, ActivationSerializer
from .tasks import send_activation_email

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        elif self.action == "activation":
            return ActivationSerializer
        return self.serializer_class

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save(*args, **kwargs)

        context = {"user_id": user.id}
        to = [user.email]
        send_activation_email.delay(context, to)

    @action(["post"], detail=False)
    def activation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
