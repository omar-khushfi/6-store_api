import django_filters
from .models import *
class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    maxprice=django_filters.filters.NumberFilter(field_name='price' or 10000,lookup_expr='gte')
    minprice=django_filters.filters.NumberFilter(field_name='price' or 0,lookup_expr='lte')
    keyword=django_filters.filters.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ('category','brand','keyword','minprice','maxprice')