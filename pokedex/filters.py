from .models import Pokemon
import django_filters

class PokeFilter(django_filters.FilterSet):
    class Meta:
        model = Pokemon
        fields = ['name', 'number']