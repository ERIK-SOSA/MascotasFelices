from rest_framework import serializers
from .models import dueños, mascotas, fichadesparacitacion, citas, estadisticasreportes, empleados, facturacionpagos, facturacionproductosmedicamentos, productosmedicamentos

class DueñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = dueños
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = mascotas
        fields = '__all__'

class FichaDesparacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = fichadesparacitacion
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = citas
        fields = '__all__'

class EstadisticasReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = estadisticasreportes
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleados
        fields = '__all__'

class FacturacionPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = facturacionpagos
        fields = '__all__'

class FacturacionProductosMedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = facturacionproductosmedicamentos
        fields = '__all__'

class ProductosMedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = productosmedicamentos
        fields = '__all__'
