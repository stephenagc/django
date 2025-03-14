from django.urls import path
from .views import game_list

urlpatterns = [
    path('', game_list, name='game_list'),
]

from django.urls import path
from .views import game_list, add_game, delete_game

urlpatterns = [
    path('', game_list, name='game_list'),
    path('add/', add_game, name='add_game'),
    path('delete/<int:game_id>/', delete_game, name='delete_game'),
]

from django.urls import path
from .views import game_list, add_game, delete_game, edit_game

urlpatterns = [
    path('', game_list, name='game_list'),
    path('add/', add_game, name='add_game'),
    path('edit/<int:game_id>/', edit_game, name='edit_game'),
    path('delete/<int:game_id>/', delete_game, name='delete_game'),
]
