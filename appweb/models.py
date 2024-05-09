import uuid
from django.db import models

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    usuario = models.IntegerField()
    contraseña = models.BooleanField()
    direccion = models.CharField(max_length=80)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Categoria(models.Model):
    id_categoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=4000)
    def __str__(self):
        return f"{self.nombre} {self.id_categoria}"

class Producto(models.Model):
    id_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=4000)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="producto",null=True)
    def __str__(self):
        return f"{self.nombre} {self.precio} {self.id_producto}"
    

class Personalizado(models.Model):
    id_personalizado = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=4000)
    apellido = models.CharField(max_length=4000)
    telefono = models.IntegerField()
    foto = models.ImageField(upload_to="producto",null=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre}  {self.id_personalizado}"





