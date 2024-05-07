from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    # Lógica para la vista de tsurikawa
    return render(request, "pagTsurikawa.html")

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
    # Lógica para la vista de otros
    return render(request, "otros.html")

def luces(request):
    # Lógica para la vista de luces
    return render(request, "luces.html")

def lip(request):
    # Lógica para la vista de lip
    return render(request, "lip.html")

def pomo(request):
    # Lógica para la vista de pomo
    return render(request, "pomo.html")

def tapaValvula(request):
    # Lógica para la vista de tapaValvula
    return render(request, "tapaValvula.html")

def cubreCaliper(request):
    # Lógica para la vista de cubreCaliper
    return render(request, "cubreCaliper.html")

def capucha(request):
    # Lógica para la vista de capucha
    return render(request, "capucha.html")

def carrito(request):
    # Lógica para la vista de carrito
    return render(request, "carrito.html")

def fabricado(request):
    # Lógica para la vista de fabricado
    return render(request, "fabricado.html")

def personalizado(request):
    # Lógica para la vista de personalizado
    return render(request, "personalizado.html")

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



