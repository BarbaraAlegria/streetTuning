from django.urls import path
from . import views 
from .views import *
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
    path('busqueda/',busquedaproducto,name="busqueda"),


    path('Mantenedor/Productos/listar/', listar_Productos , name="listar_Productos"),
    path('Mantenedor/Productos/agregar/', agregar_producto , name="agregar_producto"),
    path('Mantenedor/Productos/modificar/<id_producto>/', modificar_producto , name="modificar_producto"),
    path('eliminar_producto/<id_producto>/', eliminar_producto, name="eliminar_producto"),
     path('base', base , name="base"),




    path('pagAdmin', pagAdmin, name='pagAdmin'),



    path('checkout', views.checkout, name="checkout"),
    path('carrito',views.carrito, name='carrito'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('update_cart_quantity/', views.update_cart_quantity, name='update_cart_quantity'),
    path('get_cart_items/', views.get_cart_items, name='get_cart_items'),
    
    


]