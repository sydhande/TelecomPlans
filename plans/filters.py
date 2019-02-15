from .models import Landline, Broadband
import django_filters


class LandlineFilter(django_filters.FilterSet):
    planname = django_filters.CharFilter(lookup_expr='icontains')
    applicability = django_filters.CharFilter(lookup_expr='icontains')
    fmc = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Landline
        fields = ['planname', 'applicability', 'fmc',]


class BroadbandFilter(django_filters.FilterSet):
    planname = django_filters.CharFilter(lookup_expr='icontains')
    speed = django_filters.CharFilter(lookup_expr='icontains')
    fmc = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Broadband
        fields = ['planname', 'speed', 'fmc',]