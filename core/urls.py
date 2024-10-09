from django.urls import path
from .views import LivroList, LivroDetail, AutorList, AutorDetail, CategoriaList, CategoriaDetail

urlpatterns = [
    path('livros/', LivroList.as_view(), name='livro-list'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
    path('categorias/', CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
]

