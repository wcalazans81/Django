from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    # endereco de ip das paginas criadas na aplicação
    slug = models.SlugField(max_length=255, unique=True)
    # Autor da aplicaçao
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Corpo de texto das postagens feitas na aplicalção
    body = models.TextField()
    # Automatizar data e hora que o post foi criado na aplicação
    created = models.DateTimeField(auto_now_add=True)
    # Atualizar informações do post criado anteriormente
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
         
    