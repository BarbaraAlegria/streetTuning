from .models import Cliente, Orden

def carrito_items(request):
    if request.user.is_authenticated:
        try:
            cliente = Cliente.objects.get(usuario=request.user)
            orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
            carritoItems = orden.get_carrito_items
        except Cliente.DoesNotExist:
            carritoItems = 0
    else:
        carritoItems = 0
    
    return {'carritoItems': carritoItems}
