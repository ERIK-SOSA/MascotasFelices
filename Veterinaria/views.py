from rest_framework import viewsets
from .models import dueños, mascotas, fichadesparacitacion, citas, estadisticasreportes, empleados, facturacionpagos, facturacionproductosmedicamentos, productosmedicamentos 
from .serializers import  DueñoSerializer, MascotaSerializer, FichaDesparacitacionSerializer, CitaSerializer, EstadisticasReportesSerializer, EmpleadoSerializer, FacturacionPagosSerializer, FacturacionProductosMedicamentosSerializer, ProductosMedicamentosSerializer 

class DueñoViewSet(viewsets.ModelViewSet):
    queryset = dueños.objects.all()
    serializer_class = DueñoSerializer
    permission_classes = []


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = mascotas.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = []
    

class FichaDesparacitacionViewSet(viewsets.ModelViewSet):
    queryset = fichadesparacitacion.objects.all()
    serializer_class = FichaDesparacitacionSerializer
    permission_classes = []


class EstadisticasReportesViewSet(viewsets.ModelViewSet):
    queryset = estadisticasreportes.objects.all()
    serializer_class = EstadisticasReportesSerializer
    permission_classes = []


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = empleados.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = []


class FacturacionPagosViewSet(viewsets.ModelViewSet):
    queryset = facturacionpagos.objects.all()
    serializer_class = FacturacionPagosSerializer
    permission_classes = []


class FacturacionProductosMedicamentosViewSet(viewsets.ModelViewSet):
    queryset = facturacionproductosmedicamentos.objects.all()
    serializer_class = FacturacionProductosMedicamentosSerializer
    permission_classes = []
    

class ProductosMedicamentosViewSet(viewsets.ModelViewSet):
    queryset = productosmedicamentos.objects.all()
    serializer_class = ProductosMedicamentosSerializer
    permission_classes = []


class CitaViewSet(viewsets.ModelViewSet):
    queryset = citas.objects.all()
    serializer_class = CitaSerializer
    permission_classes = []

