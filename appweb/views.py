import logging
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect




from .forms import *
from .models import *
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

def pagTsurikawa(request):
    tsurikawa = Producto.objects.filter(categoria__id_categoria='b71c5013-d436-4e2b-902d-690b822080dd')
    data ={
        'tsurikawa' : tsurikawa
    }
    
    # Lógica para la vista de tsurikawa
    return render(request, "pagTsurikawa.html",data)

def pagOpiniones(request):
    # Lógica para la vista de opiniones y/o sugerencias
    return render(request, "pagOpiniones.html")
       
def login(request):
    print("Bienvenido "+ request.user.username)


    print("Grupos", request.user.groups.all())

    if request.user.groups.filter(name='user'):
        print("Es un user")

    return redirect(to='home')


def registro(request):
    data = {
        "mensaje": ""
    }
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            data["mensaje"] = "Las contraseñas deben ser iguales"
        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = nombre
            usu.first_name = nombre
            usu.last_name = apellido
            grupo = Group.objects.get(name='user')
            try:
                usu.save()
                usu.groups.add(grupo)
                data["mensaje"] = "Usuario creado"
                user = authenticate(username=usu.username, password=password1)
                login(request, user)
                return redirect(to='home')
            except:
                messages.error(request, msgFormNotValid)
    return render(request, "registration/registro.html", data)


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

def personalizado(request):
    data= {
        'form' : PersonalizadoForm,
        'mensaje' :""
    }
    if request.method =="POST":
        formulario= PersonalizadoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Presonalización Enviada"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"
            
    return render(request, "personalizado.html",data)

def adminSistema(request):
    # Lógica para la vista de adminSistema
    return render(request, "adminSistema.html")

def reporteria(request):
    # Lógica para la vista de reporteria
    return render(request, "reporteria.html")

def gestionUsuario(request):
    # Obtener la lista de usuarios registrados
    usuarios = User.objects.all()
    return render(request, 'gestionUsuario.html', {'usuarios': usuarios})

def adminContenido(request):
    # Lógica para la vista de adminContenido de la pantalla del administrador
    return render(request, "adminContenido.html")



################# mantenedor productos ##############
def listar_Productos(request):
    productos = Producto.objects.all()
    data = {
        "productos" : productos
    }
    return render(request, "Mantenedor/Productos/listar.html", data)

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
def pagAdmin(request):
    # Lógica para la vista de carrito
    return render(request, "pagAdmin.html")




#*************CARRITO DE COMPRA************

def carrito(request):
    # Lógica para la vista de carrito
    return render(request, "carrito.html")
def checkout(request):
      context = {}
      return render(request, 'checkout.html', context)



#**************busqueda por categoria******


def busquedaproducto(request):
    text = request.GET.get('search_text', '')
    categoria=Categoria.objects.filter(nombre=text).last()                            
    data = {
        "categoria" : categoria
    }

    return render(request, "resultado_Busqueda.html", data)