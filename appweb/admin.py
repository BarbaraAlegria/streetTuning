from django.contrib import admin
from .models import *



class PorductoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','id_producto','cantidad']
    list_editable=['precio','cantidad']
    search_fields=['id_producto']

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_orden', 'complete', 'transaccion_id')



# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto,PorductoAdmin)
admin.site.register(Personalizado)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(OrdenItem)
admin.site.register(DireccionEnvio)
admin.site.register(Opinion)
admin.site.register(Valoracion)

