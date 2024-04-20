from rest_framework import viewsets
from .models import Dueño, Mascota, FichaDesparacitacion, Cita, EstadisticasReportes, Empleado, FacturacionPagos, FacturacionProductosMedicamentos, ProductosMedicamentos 
from .serialiazers import  DueñoSerializer, MascotaSerializer, FichaDesparacitacionSerializer, CitaSerializer, EstadisticasReportesSerializer, EmpleadoSerializer, FacturacionPagosSerializer, FacturacionProductosMedicamentosSerializer, ProductosMedicamentosSerializer 

class DueñoViewSet(viewsets.ModelViewSet):
    queryset = Dueño.objects.all()
    serializer_class = DueñoSerializer
    permission_classes = []


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = []
    

class FichaDesparacitacionViewSet(viewsets.ModelViewSet):
    queryset = FichaDesparacitacion.objects.all()
    serializer_class = FichaDesparacitacionSerializer
    permission_classes = []


class EstadisticasReportesViewSet(viewsets.ModelViewSet):
    queryset = EstadisticasReportes.objects.all()
    serializer_class = EstadisticasReportesSerializer
    permission_classes = []


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = []


class FacturacionPagosViewSet(viewsets.ModelViewSet):
    queryset = FacturacionPagos.objects.all()
    serializer_class = FacturacionPagosSerializer
    permission_classes = []


class FacturacionProductosMedicamentosViewSet(viewsets.ModelViewSet):
    queryset = FacturacionProductosMedicamentos.objects.all()
    serializer_class = FacturacionProductosMedicamentosSerializer
    permission_classes = []
    

class ProductosMedicamentosViewSet(viewsets.ModelViewSet):
    queryset = ProductosMedicamentos.objects.all()
    serializer_class = ProductosMedicamentosSerializer
    permission_classes = []


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = []

