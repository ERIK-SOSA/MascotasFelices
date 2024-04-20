from rest_framework import serializers
from .models import Dueño, Mascota, FichaDesparacitacion, Cita, EstadisticasReportes, Empleado, FacturacionPagos, FacturacionProductosMedicamentos, ProductosMedicamentos

class DueñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueño
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class FichaDesparacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaDesparacitacion
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class EstadisticasReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasReportes
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class FacturacionPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturacionPagos
        fields = '__all__'

class FacturacionProductosMedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturacionProductosMedicamentos
        fields = '__all__'

class ProductosMedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosMedicamentos
        fields = '__all__'
