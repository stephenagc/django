from django.shortcuts import render

# Create your views here.
from .models import Game
from .forms import GameSearchForm

def game_list(request):
    form = GameSearchForm(request.GET)
    games = Game.objects.all()

    if form.is_valid() and form.cleaned_data['query']:
        query = form.cleaned_data['query']
        games = games.filter(title__icontains=query)

    return render(request, 'games/game_list.html', {'form': form, 'games': games})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'games/add_game.html', {'form': form})

def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        game.delete()
        return redirect('game_list')
    return render(request, 'games/delete_game.html', {'game': game})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm, GameSearchForm

def game_list(request):
    form = GameSearchForm(request.GET)
    games = Game.objects.all()

    if form.is_valid() and form.cleaned_data['query']:
        query = form.cleaned_data['query']
        games = games.filter(title__icontains=query) | games.filter(category__icontains=query)

    return render(request, 'games/game_list.html', {'form': form, 'games': games})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm

def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)

    return render(request, 'games/edit_game.html', {'form': form, 'game': game})
