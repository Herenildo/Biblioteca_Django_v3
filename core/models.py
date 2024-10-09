from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome  # Retorna o nome da categoria como representação em string


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome  # Retorna o nome do autor como representação em string


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado_em = models.DateField()
    
    def __str__(self):
        return self.titulo  # Retorna o título do livro como representação em string
