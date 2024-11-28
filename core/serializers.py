from rest_framework import serializers
from .models import Livro, Autor, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class ColecaoSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.SlugRelatedField(
        many=True,
        queryset=Livro.objects.all(),
        slug_field='titulo'
    )
    colecionador = serializers.ReadOnlyField(source='colecionador.username')

    class Meta:
        model = Colecao
        fields = ('url', 'id', 'nome', 'descricao', 'colecionador', 'livros')

