from django.contrib import admin
from .models import Pokemon, Trainer, Pokemon_List, Region, Stats, Type

admin.site.register(Pokemon)
admin.site.register(Trainer)
admin.site.register(Region)
admin.site.register(Stats)
admin.site.register(Type)
admin.site.register(Pokemon_List)