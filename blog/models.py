from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class motos(models.Model):
    marcaSeleccion = (
    ('honda','honda'),
    ('bajaj', 'bajaj'),
    ('yamaha','yamaha'),
    ('ktm','ktm'),
    ('bmw','bmw'),
    ('otro', 'otro'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=150)
    marca = models.CharField(max_length=50, choices=marcaSeleccion, default='honda')
    modelo = models.CharField(max_length=50)
    cilindrada = models.IntegerField()
    kilometro = models.IntegerField()
    color = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    telefono = models.IntegerField()
    email = models.EmailField()
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    motos = models.ForeignKey(motos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.descripcion