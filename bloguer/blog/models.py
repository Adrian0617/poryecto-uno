from django.db import models

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(verbose_name="descripcion")
    image = models.ImageField(verbose_name="imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="fecha de edicion")
    
    class Meta:
        verbose_name = 'blog'
        verbose_name = 'blog'
        ordering = ["-created"]
    
    def __str__(self):
        return self.titulo