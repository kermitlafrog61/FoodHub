from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type']
    ordering_fields = ['popularity', 'novelty', 'price']
    ordering = ['-popularity']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.popularity += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('ordering', openapi.IN_QUERY,
                              description="Ordering field", type=openapi.TYPE_STRING)
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
