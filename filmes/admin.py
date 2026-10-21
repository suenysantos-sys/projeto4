from django.contrib import admin
from .models import Generos, Filmes
from rest_framework.authtoken.models import Token

# Admin para o modelo Generos: mostra o campo 'nome' e permite busca por nome
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'ano_lancamento', 'duracao')
    list_filter = ('genero', 'ano_lancamento')
    search_fields = ('titulo', 'descricao')

admin.site.register(Token)