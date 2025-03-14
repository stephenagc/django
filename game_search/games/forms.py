from django import forms
from .models import Game

class GameSearchForm(forms.Form):
    query = forms.CharField(label="Buscar Jogo", max_length=200, required=False)


from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'category', 'release_year', 'image']

from django import forms

class GameSearchForm(forms.Form):
    query = forms.CharField(label="Buscar Jogo", required=False)
