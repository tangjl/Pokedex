from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pokemon_list, name='pokemon_list'),
]