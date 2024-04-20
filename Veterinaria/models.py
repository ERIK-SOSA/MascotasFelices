from rest_framework import serializers
from django.db import models

class Dueño(models.Model):
    DueñoID = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=20)
    CorreoElectronico = models.EmailField()

    def __str__(self):
        return 'Dueño ID: ' + str(self.DueñoID) + ' / Dueño: ' + self.Nombres + ' ' + self.Apellidos

class Mascota(models.Model):
    MascotaID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Especie = models.CharField(max_length=100)
    Raza = models.CharField(max_length=100)
    Edad = models.PositiveIntegerField()
    Seño = models.CharField(max_length=100)
    FechaNacimiento = models.DateField()
    Color = models.CharField(max_length=100)
    Peso = models.DecimalField(max_digits=5, decimal_places=2)
    NotasAdicionales = models.TextField()
    DueñoID = models.ForeignKey(Dueño, on_delete=models.CASCADE)

    def __str__(self):
        return 'Mascota ID: ' + str(self.MascotaID) + ' / Nombre: ' + self.Nombre

class FichaDesparacitacion(models.Model):
    FichaDesparacitacionID = models.AutoField(primary_key=True)
    FechaDesparacitacion = models.DateField()
    TipoDesparacitacion = models.CharField(max_length=100)
    Dosis = models.CharField(max_length=100)
    NotasAdicionales = models.TextField()
    MascotaID = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return 'Ficha ID: '+ str(self.FichaDesparacitacionID)

class Cita(models.Model):
    CitaID = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Hora = models.TimeField()
    MotivoVisita = models.CharField(max_length=200)
    Estado = models.CharField(max_length=100)
    Observaciones = models.TextField()
    MascotaID = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    EmpleadoID = models.ForeignKey('Empleado', on_delete=models.CASCADE)

    def __str__(self):
        return 'Cita ID: ' + str(self.CitaID)

class EstadisticasReportes(models.Model):
    EstadisticasReportesID = models.AutoField(primary_key=True)
    CitasAtendidas = models.PositiveIntegerField()
    TipoServiciosSolicitados = models.CharField(max_length=200)
    IngresosGenerados = models.DecimalField(max_digits=10, decimal_places=2)
    OtrosDatosEstadisticos = models.TextField()
    CitaID = models.ForeignKey(Cita, on_delete=models.CASCADE)

    def __str__(self):
        return 'Reporte ID: ' + str(self.EstadisticasReportesID)

class Empleado(models.Model):
    EmpleadoID = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)
    HorarioTrabajo = models.CharField(max_length=100)
    CorreoElectronico = models.EmailField()
    Telefono = models.CharField(max_length=20)

    def __str__(self):
        return 'Empleado ID: '+ str(self.EmpleadoID) + ' / Empleado:' + self.Nombres + ' ' + self.Apellidos

class FacturacionPagos(models.Model):
    FacturaID = models.AutoField(primary_key=True)
    NumeroFactura = models.CharField(max_length=100)
    FechaEmision = models.DateField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    MetodoPago = models.CharField(max_length=100)
    EstadoPago = models.CharField(max_length=100)
    DetallePago = models.TextField()
    CitaID = models.ForeignKey(Cita, on_delete=models.CASCADE)

    def __str__(self):
        return 'Factura ID: ' + str(self.FacturaID) + ' / Total'  + str(self.Total)

class FacturacionProductosMedicamentos(models.Model):
    FacturacionProductosMedicamentosID = models.AutoField(primary_key=True)
    FacturaID = models.ForeignKey(FacturacionPagos, on_delete=models.CASCADE)
    ProductoID = models.ForeignKey('ProductosMedicamentos', on_delete=models.CASCADE)
    Cantidad = models.PositiveIntegerField()

    def __str__(self):
        return 'Facturación ID: ' + str(self.FacturacionProductosMedicamentosID)

class ProductosMedicamentos(models.Model):
    ProductoID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    CantidadInventario = models.PositiveIntegerField()
    Proveedor = models.CharField(max_length=100)

    def __str__(self):
        return 'Producto ID: ' + str(self.ProductoID) + ' / Nombre: ' + self.Nombre
