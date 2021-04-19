import django_filters
from .models import Article


class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    views_more = django_filters.NumberFilter(field_name='views', lookup_expr='gt')
    views_less = django_filters.NumberFilter(field_name='views', lookup_expr='lt')

    class Meta:
        model = Article
        fields = ('title',)
