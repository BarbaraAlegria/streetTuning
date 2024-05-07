from django.urls import path
from . import views
from .views import home, pagAccesorios, pagStickers, pagTsurikawa, login, registro, pagOpiniones, otros, luces, lip, pomo, tapaValvula, cubreCaliper, capucha, carrito, fabricado, personalizado, adminSistema, reporteria, gestionUsuario, adminContenido
urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('pagAccesorios', pagAccesorios, name="pagAccesorios"),
    path('pagStickers', pagStickers, name="pagStickers"),
    path('pagTsurikawa', pagTsurikawa, name="pagTsurikawa"),
    path('pagOpiniones', pagOpiniones, name='pagOpiniones'),
    path('login', login, name='login'),
    path('registro', registro, name='registro'),
    path('otros', otros, name='otros'),
    path('luces', luces, name='luces'),
    path('lip', lip, name='lip'),
    path('pomo', pomo, name='pomo'),
    path('tapaValvula', tapaValvula, name='tapaValvula'),
    path('cubreCaliper', cubreCaliper, name='cubreCaliper'),
    path('capucha', capucha, name='capucha'),
    path('carrito', carrito, name='carrito'),
    path('fabricado', fabricado, name='fabricado'),
    path('personalizado', personalizado, name='personalizado'),
    path('adminSistema', adminSistema, name='adminSistema'),
    path('reporteria', reporteria, name='reporteria'),
    path('gestionUsuario', gestionUsuario, name='gestionUsuario'),
    path('adminContenido/', views.adminContenido, name='adminContenido'),


]