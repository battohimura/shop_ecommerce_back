from rest_framework import generics
from rest_framework.response import Response

from .models import Product
from .serializers import ListProductSerializer


class ListProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ListProductSerializer(queryset, many=True)
        return Response(serializer.data)
