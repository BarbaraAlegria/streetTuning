import json
import logging
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import *
import csv
logger = logging.getLogger(__name__)
msgFormNotValid="Formulario no valido"

# Create your views here.
def home(request):
    return render(request, "home.html")

def pagAccesorios(request):
    # Lógica para la vista de accesorios
    return render(request, "pagAccesorios.html")

def pagStickers(request):
    # Lógica para la vista de stickers
    return render(request, "pagStickers.html")
def gestionUsuarios(request):
    # Lógica para la vista de stickers
    return render(request, "gestionUsuarios.html")

def pagTsurikawa(request):
    tsurikawa = Producto.objects.filter(categoria__id_categoria='b71c5013-d436-4e2b-902d-690b822080dd')
    data ={
        'tsurikawa' : tsurikawa
    }
    
    # Lógica para la vista de tsurikawa
    return render(request, "pagTsurikawa.html",data)

def pagOpiniones(request):
    data= {
        'form' : OpinionForm,
        'mensaje' :""
    }
    if request.method =="POST":
        formulario= OpinionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Sugerencia Enviada")
            return redirect(to="pagAccesorios")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"
    return render(request, "pagOpiniones.html",data)
       
def login(request):
    print("Bienvenido "+ request.user.username)


    print("Grupos", request.user.groups.all())

    if request.user.groups.filter(name='user').exists():
        print("Es un user")

    return redirect(to='home')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data['password1']
            usuario.set_password(password)
            usuario.save()
            grupo = Group.objects.get(name='user')
            usuario.groups.add(grupo)
            Cliente.objects.create(
                usuario=usuario,
                nombre=form.cleaned_data['first_name'],
                apellido=form.cleaned_data['last_name'],
                rut=form.cleaned_data.get('rut', '')  # Ajusta este campo según tus necesidades
            )
            # Autenticar y loguear al usuario
            user = authenticate(username=usuario.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Hubo un error al autenticar el usuario.")
        else:
            messages.error(request, "Formulario inválido.")
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


def otros(request):
    otros = Producto.objects.filter(categoria__id_categoria='67de268a-218c-4bdb-a881-db47a68331ba')
    data ={
        'otros' : otros
    }
    return render(request, "otros.html",data)

def luces(request):
    luces = Producto.objects.filter(categoria__id_categoria='82b3b0ea-da68-4f58-92f6-66638a08701d')
    data ={
        'luces' : luces
    }
    return render(request, 'luces.html', data)

    

def lip(request):
    lip = Producto.objects.filter(categoria__id_categoria='95b79381-966f-40bb-adc1-7434b5f020ea')
    data ={
        'lip' : lip
    }
    return render(request, "lip.html",data)

def pomo(request):
    pomo = Producto.objects.filter(categoria__id_categoria='6b252979-fae6-431f-b2c8-055d7f203aa0')
    data ={
        'pomo' : pomo
    }
    return render(request, "pomo.html",data)

def tapaValvula(request):
    tapaValvula = Producto.objects.filter(categoria__id_categoria='080ceb12-048c-4dff-9543-9b6d36708939')
    data ={
        'tapaValvula' : tapaValvula
    }
    return render(request, "tapaValvula.html",data)

def cubreCaliper(request):
    cubreCaliper = Producto.objects.filter(categoria__id_categoria='09c00024-2c9c-484c-a06c-3558c40ca152')
    data ={
        'cubreCaliper' : cubreCaliper
    }
    return render(request, "cubreCaliper.html",data)

def capucha(request):
    capucha = Producto.objects.filter(categoria__id_categoria='3b9be3c4-a5ff-48e2-9c6e-f2b8df4861be')
    data ={
        'capucha' : capucha
    }
    return render(request, "capucha.html",data)



def fabricado(request):
    # Lógica para la vista de fabricado
    return render(request, "fabricado.html")

def listar_personalizados(request):
    personalizado = Personalizado.objects.all()
    data = {
        "personalizado" : personalizado
    }
    return render(request, "Mantenedor/personalizado/listar.html", data)

def personalizado(request):
    data= {
        'form' : PersonalizadoForm,
        'mensaje' :""
    }
    if request.method =="POST":
        formulario= PersonalizadoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud enviada")
            return redirect(to="pagAccesorios")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"
            
    return render(request, "personalizado.html",data)

def eliminar_personalizado(request, id_personalizado):
    personalizado = get_object_or_404(Personalizado, id_personalizado=id_personalizado)
    personalizado.delete()
    return redirect(to="listar_personalizados")


def adminSistema(request):
    # Lógica para la vista de adminSistema
    return render(request, "adminSistema.html")


def gestionUsuario(request):
    # Obtener la lista de usuarios registrados
    usuarios = User.objects.all()
    return render(request, 'gestionUsuario.html', {'usuarios': usuarios})

def adminContenido(request):
    # Lógica para la vista de adminContenido de la pantalla del administrador
    return render(request, "adminContenido.html")
################# mantenedor envios ##############
def listar_envios(request):
    estado = request.GET.get('estado')
    if estado:
        envios = DireccionEnvio.objects.filter(Estado=estado).order_by('-fecha_agregado')
    else:
        envios = DireccionEnvio.objects.all().order_by('-fecha_agregado')
    
    context = {
        'envios': envios,
    }
    return render(request, "Mantenedor/Envios/listar.html", context)
def despacho_envio(request, id):
    envio = get_object_or_404(DireccionEnvio, id=id)
    envio.Estado='En Camino'
    envio.save()
    messages.success(request, "Pedido en Ruta")
    return redirect(to="listar_envios")

def entrega_envio(request, id):
    recibidoPor=request.GET.get('recibidoPor', '')
    envio = get_object_or_404(DireccionEnvio, id=id)
    envio.Estado='Entregado'
    envio.recibido=recibidoPor

    envio.save()
    messages.success(request, "Envio Entregado")
    return redirect(to="listar_envios")


################# mantenedor opiniones ##############
def listar_opinion(request):
    opinion = Opinion.objects.all()
    data = {
        "opinion" : opinion
    }
    return render(request, "Mantenedor/Opiniones/listar.html", data)

def eliminar_opinion(request, id):
    opinion = get_object_or_404(Opinion, id=id)
    opinion.delete()
    return redirect(to="listar_opinion")


################# mantenedor productos ##############
def listar_Productos(request):
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'Mantenedor/Productos/listar.html', {'productos': productos, 'categorias': categorias})


def agregar_producto(request):
    if request.method == "POST":
        formulario = ProductForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado con éxito")
            return redirect(to="listar_Productos")
        else:
            messages.error(request, "Error al agregar el producto. Por favor, revise el formulario.")

    data = {
        'form': ProductForm()
    }
    
    return render(request, "mantenedor/Productos/agregar.html", data)



def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    producto.delete()
    return redirect(to="listar_Productos")

def modificar_producto(request,id_producto):

    producto = get_object_or_404(Producto, id_producto=id_producto)

    data = {
        "form": ProductForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El Producto se ha modificado con exito")
            return redirect(to="listar_Productos")
        else:
            messages.error(request, msgFormNotValid)
            data["form"] =  formulario
    return render(request, "mantenedor/Productos/modificar.html",data)



#Tareas del administrador 
@login_required(login_url='/accounts/login')
@permission_required(['appweb.view_atencion'], login_url='/accounts/login')
def pagAdmin(request):
    # Lógica para la vista de carrito
    return render(request, "pagAdmin.html")




def carrito(request):
    if request.user.is_authenticated:
        # Intenta obtener el cliente relacionado con el usuario autenticado
        try:
            cliente = Cliente.objects.get(usuario=request.user)
            orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
            items = orden.ordenitem_set.all()
        except Cliente.DoesNotExist:
            # Si no existe un cliente para el usuario, maneja la situación (e.g., mostrar mensaje o crear perfil de cliente)
            items = []
            orden = {'get_carrito_total':0, 'get_carrito_items':0}
            # Puedes elegir renderizar la misma página con un mensaje de error o manejar de otra forma
    else:
        items = []
        orden = {'get_carrito_total':0, 'get_carrito_items':0}
    
    context = {'items': items, 'orden': orden}
    return render(request, "carrito.html", context)
def checkout(request):
      
    if request.user.is_authenticated:
        # Intenta obtener el cliente relacionado con el usuario autenticado
        try:
            cliente = Cliente.objects.get(usuario=request.user)
            orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
            items = orden.ordenitem_set.all()
        except Cliente.DoesNotExist:
            # Si no existe un cliente para el usuario, maneja la situación (e.g., mostrar mensaje o crear perfil de cliente)
            items = []
            orden = {'get_carrito_total':0, 'get_carrito_items':0}
            # Puedes elegir renderizar la misma página con un mensaje de error o manejar de otra forma
    else:
        items = []
        orden = {'get_carrito_total':0, 'get_carrito_items':0}
    
    context = {'items': items, 'orden': orden}
    return render(request, 'checkout.html', context)

@csrf_exempt
def update_cart(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    user = request.user
    cliente, created = Cliente.objects.get_or_create(usuario=user)
    producto = Producto.objects.get(id_producto=product_id)
    orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
    orden_item, created = OrdenItem.objects.get_or_create(orden=orden, Producto=producto)

    if action == 'add':
        if orden_item.cantidadProducto < producto.cantidad:
            orden_item.cantidadProducto += 1
        else:
            return JsonResponse({'status': 'error', 'message': 'No hay suficiente stock disponible.'}, safe=False)
    elif action == 'remove':
        orden_item.cantidadProducto -= 1

    orden_item.save()

    if orden_item.cantidadProducto <= 0:
        orden_item.delete()

    return JsonResponse({'status': 'success', 'cart_items': orden.get_carrito_items}, safe=False)


@csrf_exempt
def update_cart_quantity(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    user = request.user
    cliente, created = Cliente.objects.get_or_create(usuario=user)
    producto = Producto.objects.get(id_producto=product_id)
    orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
    orden_item, created = OrdenItem.objects.get_or_create(orden=orden, Producto=producto)

    if action == 'add':
        if orden_item.cantidadProducto < producto.cantidad:
            orden_item.cantidadProducto += 1
        else:
            return JsonResponse({'status': 'error', 'message': 'No hay suficiente stock disponible.'}, safe=False)
    elif action == 'remove':
        orden_item.cantidadProducto -= 1

    orden_item.save()

    if orden_item.cantidadProducto <= 0:
        orden_item.delete()

    return JsonResponse({'status': 'success', 'cart_items': orden.get_carrito_items}, safe=False)

def base(request):
    if request.user.is_authenticated:
        try:
            cliente = Cliente.objects.get(usuario=request.user)
            orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
            items = orden.ordenitem_set.all()
            carritoItems = orden.get_carrito_items
        except Cliente.DoesNotExist:
            items = []
            orden = {'get_carrito_total':0, 'get_carrito_items':0}
            carritoItems = orden['get_carrito_items']
    else:
        items = []
        orden = {'get_carrito_total':0, 'get_carrito_items':0}
        carritoItems = orden['get_carrito_items']
    
    context = {'items': items, 'orden': orden, 'carritoItems': carritoItems}
    return render(request, 'base.html', context)

def get_cart_items(request):
    if request.user.is_authenticated:
        try:
            cliente = Cliente.objects.get(usuario=request.user)
            orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
            cart_items = orden.get_carrito_items
        except Cliente.DoesNotExist:
            cart_items = 0
    else:
        cart_items = 0

    return JsonResponse({'cart_items': cart_items}, safe=False)



def submit_shipping(request):
    if request.method == 'POST':
        address = request.POST['address']
        city = request.POST['city']
        comuna = request.POST['state']
        codigo_postal = request.POST['zipcode']

        # Validación básica
        if not all([address, city, comuna, codigo_postal]):
            return HttpResponse("Todos los campos son obligatorios.", status=400)

        # Obtener el cliente y la orden asociados al usuario logueado
        user = request.user
        cliente = Cliente.objects.filter(usuario=user).first()
        if not cliente:
            return HttpResponse("Cliente no encontrado.", status=404)
        
        orden = Orden.objects.filter(cliente=cliente, complete=False).first()
        if not orden:
            return HttpResponse("Orden no encontrada.", status=404)

        # Guardar la dirección de envío
        DireccionEnvio.objects.create(
            cliente=cliente,
            orden=orden,
            direccion=address,
            ciudad=city,
            comuna=comuna,
            codigoPostal=codigo_postal
        )

        # Actualizar el stock de productos y completar la orden
        orden_items = OrdenItem.objects.filter(orden=orden)
        for item in orden_items:
            producto = item.Producto
            producto.cantidad -= item.cantidadProducto
            if producto.cantidad < 0:
                return HttpResponse(f"Stock insuficiente para el producto {producto.nombre}", status=400)
            producto.save()

        # Marcar la orden como completa
        orden.complete = True
        orden.save()
        messages.success(request, "Tu orden está en preparación, Animate y dinos tu experiencia ")

        return render(request, "calificaciones.html")
    # Obtener la información del usuario logueado
    user = request.user
    cliente = Cliente.objects.filter(usuario=user).first()
    
        # manejar otros métodos o errores
        
    return redirect(to="misCompras")

      # Reemplaza con tu plantilla


#**************busqueda por categoria******

def busquedaproducto(request):
    text = request.GET.get('search_text', '')
    categoria=Categoria.objects.filter(nombre=text).last()                            
    data = {
        "categoria" : categoria
    }

    return render(request, "resultado_Busqueda.html", data)




def mostrar_ventas(request):
    ordenes_completadas = Orden.objects.filter(complete=True).prefetch_related('ordenitem_set__Producto').order_by('-fecha_orden')
    
    lista_ordenes = []
    total_general = 0  # Inicializa el total general
     # Calcular ventas totales por categoría
    ventas_por_categoria = Producto.objects.filter(
        ordenitem__orden__complete=True
    ).values('categoria__nombre').annotate(
        total_vendido=Sum('ordenitem__cantidadProducto')
    ).order_by('-total_vendido')

    total_categorias = sum(item['total_vendido'] for item in ventas_por_categoria)

    categorias_nombres = []
    categorias_porcentajes = []
    for categoria in ventas_por_categoria:
        porcentaje = (categoria['total_vendido'] / total_categorias) * 100
        categorias_nombres.append(categoria['categoria__nombre'])
        categorias_porcentajes.append(round(porcentaje, 2))

    for orden in ordenes_completadas:
        total_orden = orden.get_carrito_total  # Calcula el total de cada orden
        total_general += total_orden  # Suma al total general

        orden_dict = {
            'transaccion_id': orden.transaccion_id,
            'fecha_orden': orden.fecha_orden,
            'total_orden': total_orden,
            'items': []
        }

        items_orden = orden.ordenitem_set.all()
        for item in items_orden:
            item_dict = {
                'producto_nombre': item.Producto.nombre,
                'producto_precio': item.Producto.precio,
                'cantidad_comprada': item.cantidadProducto,
                'total_item': item.get_total
            }
            orden_dict['items'].append(item_dict)
        
        lista_ordenes.append(orden_dict)

    return render(request, 'ventas.html', {'ordenes': lista_ordenes, 'total_general': total_general,'categorias_nombres': categorias_nombres,
        'categorias_porcentajes': categorias_porcentajes })

       
def usuarios_ordenes_completadas(request):
    # Obtener todos los clientes que tienen al menos una orden
    clientes = Cliente.objects.filter(orden__isnull=False).distinct()
    

    # Preparar los datos de cada cliente
    datos_clientes = []
    for cliente in clientes:
        ordenes_cliente = Orden.objects.filter(cliente=cliente)
        
        # Preparar detalles de las órdenes
        ordenes_detalle = []
        for orden in ordenes_cliente:
            items = orden.ordenitem_set.all()
            productos_detalle = [{
                'nombre_producto': item.Producto.nombre,
                'precio_unitario': item.Producto.precio,
                'cantidad': item.cantidadProducto,
                'subtotal': item.get_total
            } for item in items]

            ordenes_detalle.append({
                'productos': productos_detalle,
                'completada': orden.complete,
                'total_orden': orden.get_carrito_total
            })

        datos_clientes.append({
            'nombre': cliente.nombre + " " + cliente.apellido,
            'email': cliente.usuario.email if cliente.usuario else "No Email",
            'ordenes_detalle': ordenes_detalle,
        })

    return render(request, 'reporteUsuario.html', {'clientes': datos_clientes})


####++++++++++++Mis compras+++++++++++++++
@login_required
def misCompras(request):
    cliente = Cliente.objects.filter(usuario=request.user, orden__complete=True).distinct().first()
    if not cliente:
        return HttpResponse("No hay órdenes completadas para mostrar.")

    # Ordenar las órdenes por 'fecha_orden' de forma descendente
    ordenes_cliente = Orden.objects.filter(cliente=cliente, complete=True).order_by('-fecha_orden')
    
    ordenes_detalle = []
    for orden in ordenes_cliente:
        items = orden.ordenitem_set.all()
        direccion_envio = DireccionEnvio.objects.filter(orden=orden).first()

        productos_detalle = [{
            'nombre_producto': item.Producto.nombre,
            'precio_unitario': item.Producto.precio,
            'cantidad': item.cantidadProducto,
            'subtotal': item.get_total,
            'foto_url': item.Producto.foto.url if item.Producto.foto else None
        } for item in items]

        ordenes_detalle.append({
            'fecha': orden.fecha_orden,
            'productos': productos_detalle,
            'estado_envio': direccion_envio.Estado if direccion_envio else 'No disponible',
            'total_orden': orden.get_carrito_total
        })

    return render(request, 'misCompras.html', {
        'cliente': cliente.nombre + " " + cliente.apellido,
        'email': cliente.usuario.email,
        'ordenes_detalle': ordenes_detalle
    })

@login_required
@csrf_protect
def submit_rating(request):
    if request.method == "POST":
        rating = request.POST.get("rating")
        review = request.POST.get("review")

        # Guarda la calificación y el comentario en la base de datos
        Rating.objects.create(rating=rating, review=review)
        messages.success(request, "Gracias por tu tiempo")

        return redirect('misCompras')  # Redirige a la página de calificaciones

    return render(request, 'calificaciones.html')

def lista_calificaciones(request):
    rating = Rating.objects.all()
    range_ = range(1, 6) 
    data ={
        'rating' : rating,
        'range' : range_
        
    }
    return render(request, "home.html",data)

