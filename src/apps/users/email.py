from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from templated_mail.mail import BaseEmailMessage

from .models import UserActivationToken

User = get_user_model()


class ActivationEmail(BaseEmailMessage):
    template_name = "email/activation.html"

    def get_context_data(self):
        context = super().get_context_data()

        user = get_object_or_404(User, id=context.get("user_id"))
        context["token"] = UserActivationToken.objects.create(user=user).token
        return context
