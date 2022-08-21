import django_filters
from .models import Result

class ResultFilter(django_filters.FilterSet):
    class Meta:
        model = Result
        fields = {
            'user__username': ['icontains'],
            'user__first_name': ['icontains'],
        }