from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['products']


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ('title',)
