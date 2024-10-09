from django.http import HttpResponse
from rest_framework import generics
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer


def home(request):
    
    html = """
    <html>
        <head>
            <title>Página Inicial</title>
        </head>
        <body>
            <h1>Bem-vindo à Biblioteca!</h1>
            <p>Você pode acessar as seguintes URLs:</p>
            <ul>
                <li><a href="/admin/">Admin</a></li>
                <li><a href="/api/livros/">API</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html)

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

