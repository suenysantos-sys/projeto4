from .models import Filmes, Generos
from .serializers import FilmesSerializer, GenerosSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

class FilmesViewSet(viewsets.ModelViewSet):
  
   queryset = Filmes.objects.all()         # queryset base para operações do ViewSet
   serializer_class = FilmesSerializer     # serializer usado para livros
   filter_backends = [DjangoFilterBackend]  # habilita filtragem via django-filter
   # campos permitidos para filtragem via query string, ex: ?titulo=foo or ?autor__nome=Silva
   filterset_fields = ['titulo', 'ano_lancamento', 'genero', 'descricao', 'duracao']

