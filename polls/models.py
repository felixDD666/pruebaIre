from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    Titulo = models.CharField(max_length=200)
    Contenido = models.TextField()
    Fecha_Creacion = models.DateTimeField('Fecha de creacion')
    PUBLICO = 'pub'
    PRIVADO = 'pri'
    pORp_choices = (
        (PUBLICO, 'publico'),
        (PRIVADO, 'privado'),
    )
    Publico_Privado = models.CharField(
        max_length=3,
        choices=pORp_choices,
        default=PUBLICO,
    )
    Foto = models.ImageField(upload_to='postPhotos', default = 'SOMETHING')
    def __str__(self):
        return self.Titulo
