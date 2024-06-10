import uuid
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Categoria(models.Model):
    id_categoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=4000)
    def __str__(self):
        return f"{self.nombre}"

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
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    foto = models.ImageField(upload_to="producto",null=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre}  {self.id_personalizado}"
    


class Orden(models.Model):
    cliente= models.ForeignKey(Cliente ,on_delete=models.CASCADE, blank=True, null=True)
    fecha_orden= models.DateTimeField(auto_now_add=True)
    complete =  models.BooleanField(default=False, null=True, blank=True)
    transaccion_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def __str__(self):
        return f"{self.transaccion_id}"
    
       
    @property
    def get_carrito_total(self):
        ordenItems = self.ordenitem_set.all()
        total= sum([item.get_total for item in ordenItems])
        return total
    
    @property
    def get_carrito_items(self):
        ordenItems = self.ordenitem_set.all()
        total= sum([item.cantidadProducto for item in ordenItems])
        return total

    
class OrdenItem(models.Model):
    Producto=models.ForeignKey(Producto ,on_delete=models.CASCADE, blank=True, null=True)
    orden = models.ForeignKey(Orden ,on_delete=models.CASCADE, blank=True, null=True)
    cantidadProducto= models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidadProducto} {self.Producto}"
    
    @property
    def get_total(self):
        total = self.Producto.precio * self.cantidadProducto
        return total
    


class DireccionEnvio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=False)
    ciudad = models.CharField(max_length=200, null=False)
    comuna = models.CharField(max_length=200, null=False)
    codigoPostal = models.CharField(max_length=200, null=False)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    Estado = models.CharField(max_length=50, default='Pendiente')
    recibido = models.CharField(max_length=200, null=True)



    def __str__(self):
        return f"{self.cliente} {self.direccion}"




class Opinion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=4000)
    email = models.EmailField(max_length=254)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre}  {self.id}"