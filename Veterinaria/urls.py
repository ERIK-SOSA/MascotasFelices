from django.urls import path
from .views import DueñoViewSet, MascotaViewSet, FichaDesparacitacionViewSet, EstadisticasReportesViewSet, EmpleadoViewSet, FacturacionPagosViewSet, FacturacionProductosMedicamentosViewSet, ProductosMedicamentosViewSet, CitaViewSet

urlpatterns = [
    # DueñoViewSet
    path('dueños/', DueñoViewSet.as_view({'get': 'list', 'post': 'create'}), name='dueños-list'),
    path('dueños/<int:pk>/', DueñoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='dueño-detail'),
    
    # MascotaViewSet
    path('mascotas/', MascotaViewSet.as_view({'get': 'list', 'post': 'create'}), name='mascotas-list'),
    path('mascotas/<int:pk>/', MascotaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='mascota-detail'),
    
    # FichaDesparacitacionViewSet
    path('fichas-desparacitacion/', FichaDesparacitacionViewSet.as_view({'get': 'list', 'post': 'create'}), name='fichas-desparacitacion-list'),
    path('fichas-desparacitacion/<int:pk>/', FichaDesparacitacionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='ficha-desparacitacion-detail'),

    # EstadisticasReportesViewSet
    path('estadisticas-reportes/', EstadisticasReportesViewSet.as_view({'get': 'list', 'post': 'create'}), name='estadisticas-reportes-list'),
    path('estadisticas-reportes/<int:pk>/', EstadisticasReportesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='estadisticas-reportes-detail'),

    # EmpleadoViewSet
    path('empleados/', EmpleadoViewSet.as_view({'get': 'list', 'post': 'create'}), name='empleados-list'),
    path('empleados/<int:pk>/', EmpleadoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='empleado-detail'),

    # FacturacionPagosViewSet
    path('facturacion-pagos/', FacturacionPagosViewSet.as_view({'get': 'list', 'post': 'create'}), name='facturacion-pagos-list'),
    path('facturacion-pagos/<int:pk>/', FacturacionPagosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='facturacion-pagos-detail'),

    # FacturacionProductosMedicamentosViewSet
    path('facturacion-productos-medicamentos/', FacturacionProductosMedicamentosViewSet.as_view({'get': 'list', 'post': 'create'}), name='facturacion-productos-medicamentos-list'),
    path('facturacion-productos-medicamentos/<int:pk>/', FacturacionProductosMedicamentosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='facturacion-productos-medicamentos-detail'),

    # ProductosMedicamentosViewSet
    path('productos-medicamentos/', ProductosMedicamentosViewSet.as_view({'get': 'list', 'post': 'create'}), name='productos-medicamentos-list'),
    path('productos-medicamentos/<int:pk>/', ProductosMedicamentosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='productos-medicamentos-detail'),

    # CitaViewSet
    path('citas/', CitaViewSet.as_view({'get': 'list', 'post': 'create'}), name='citas-list'),
    path('citas/<int:pk>/', CitaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='cita-detail'),
]