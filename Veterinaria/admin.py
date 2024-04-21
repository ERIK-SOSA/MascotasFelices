from django.contrib import admin

from .models import dueños, mascotas, fichadesparacitacion, citas, estadisticasreportes, empleados, facturacionpagos, facturacionproductosmedicamentos, productosmedicamentos

admin.site.register(dueños)
admin.site.register(mascotas)
admin.site.register(fichadesparacitacion)
admin.site.register(citas)
admin.site.register(estadisticasreportes)
admin.site.register(empleados)
admin.site.register(facturacionpagos)
admin.site.register(facturacionproductosmedicamentos)
admin.site.register(productosmedicamentos)
