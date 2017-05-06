from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pokemon_list, name='pokemon_list'),
    url(r'^search', views.search, name='search'),
    url(r'^search/[?]q=$', views.pokemon_list, name='pokemon_search'),
    url(r'^user/(?P<username>)', views.pokemon_collection, name='pokemon_collection'),
]