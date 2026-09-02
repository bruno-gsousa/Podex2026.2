from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/criar/', views.criar_pokemon,name="criar_pokemon"),
    path('pokemon/<int:pk>/editar',views.editar_pokemon,name='editar_pokemon'),
    path('pokemon/<int:pk>/deletar',views.deletar_pokemon,name='deletar_pokemon'),
    path('pokemon/listar/', views.listar_pokemons,name='listar_pokemons'),
]