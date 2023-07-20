from django_filters import rest_framework

from .models import Pereval_added


class PerevalFilter(rest_framework.FilterSet):
    users__email = rest_framework.CharFilter(field_name='users__email')

    class Meta:
        model = Pereval_added
        fields = ['users__email']
