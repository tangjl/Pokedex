from django.db import models
from django.forms import ModelForm

class PokeForm(ModelForm):
    class Meta:
        model = Region

