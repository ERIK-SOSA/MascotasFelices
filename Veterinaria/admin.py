from django.contrib import admin

from .models import Dueño, Mascota, FichaDesparacitacion, Cita, EstadisticasReportes, Empleado, FacturacionPagos, FacturacionProductosMedicamentos, ProductosMedicamentos

admin.site.register(Dueño)
admin.site.register(Mascota)
admin.site.register(FichaDesparacitacion)
admin.site.register(Cita)
admin.site.register(EstadisticasReportes)
admin.site.register(Empleado)
admin.site.register(FacturacionPagos)
admin.site.register(FacturacionProductosMedicamentos)
admin.site.register(ProductosMedicamentos)
