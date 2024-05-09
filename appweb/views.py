from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import *
from .models import *

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
    # Lógica para el inicio de sesión
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

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

def carrito(request):
    # Lógica para la vista de carrito
    return render(request, "carrito.html")

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







