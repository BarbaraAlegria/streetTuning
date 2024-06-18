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
    
    path('gestionUsuario', gestionUsuario, name='gestionUsuario'),
    path('adminContenido/', views.adminContenido, name='adminContenido'),
    path('busqueda/',busquedaproducto,name="busqueda"),


    path('Mantenedor/Productos/listar/', listar_Productos , name="listar_Productos"),
    path('Mantenedor/Productos/agregar/', agregar_producto , name="agregar_producto"),
    path('Mantenedor/Productos/modificar/<id_producto>/', modificar_producto , name="modificar_producto"),
    path('eliminar_producto/<id_producto>/', eliminar_producto, name="eliminar_producto"),
    path('base', base , name="base"),


    path('Mantenedor/Opiniones/listar/', listar_opinion , name="listar_opinion"),
    path('eliminar_opinion/<id>/', eliminar_opinion, name="eliminar_opinion"),


    path('Mantenedor/personalizado/listar/', listar_personalizados , name="listar_personalizados"),
    path('eliminar_personalizado/<id_personalizado>/', eliminar_personalizado, name="eliminar_personalizado"),

    path('Mantenedor/Envios/listar/', listar_envios , name="listar_envios"),

    path('despacho_envio/<id>/', despacho_envio, name="despacho_envio"),
    path('entrega_envio/<id>/', entrega_envio, name="entrega_envio"),











    path('pagAdmin', pagAdmin, name='pagAdmin'),



    path('checkout', views.checkout, name="checkout"),
    path('carrito',views.carrito, name='carrito'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('update_cart_quantity/', views.update_cart_quantity, name='update_cart_quantity'),
    path('get_cart_items/', views.get_cart_items, name='get_cart_items'),
    path('checkout/', views.submit_shipping, name='submit_shipping'),
    path('gestionUsuarios', gestionUsuarios, name="gestionUsuarios"),
    
    
    path('ventas/', mostrar_ventas, name='mostrar-ventas'),
    path('reporteUsuarios/', usuarios_ordenes_completadas, name='reporte_usuarios'),
    
    
    
    path('misCompras/',views.misCompras, name='misCompras'),
    path('calificaciones/',views.calificaciones, name='calificaciones'),

]