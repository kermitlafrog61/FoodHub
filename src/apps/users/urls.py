from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from . import views

User = get_user_model()

urlpatterns = [
    path('register/', views.UserViewSet.as_view({'post': 'create'})),
    path('activation/', views.UserViewSet.as_view({'post': 'activation'})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
