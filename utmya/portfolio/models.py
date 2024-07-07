from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200, verbose_name = "Titulo")
    descripcion = models.TextField(verbose_name = "Descripción")
    imagen = models.ImageField(verbose_name = "Imagen", upload_to="Proyectos")
    creado = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name = "Última fecha de edición")
   
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-creado"]
    def __str__(self):
        return self.titulo
      

