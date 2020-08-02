import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_orm.settings')
django.setup()

from factura.models import *

# INSERTAR REGISTROS EN LOS MODELOS
# PRODUCTO
p = Producto(descripcion='Laptop Hp', precio=700.50, stock=20)
p.save()
Producto.objects.create(descripcion='Mouse Logitech', precio=30.5, stock=10)
# CLIENTE
c = Cliente(ruc='0928541556001', nombre='Joan Campos', direccion='Av.Colon')
c.save()
c.producto.add(1, 2)
Cliente.objects.create(ruc='0928541556001', nombre='Carlos Cabrera', direccion='Av. Colon')
c1 = Cliente.objects.get(id=2)
c1.producto.add(1, 2)

# FACTURA
cliente = Cliente.objects.get(id=1)
f = Factura(cliente=cliente, total=500.04)
f.save()

cliente2 = Cliente.objects.get(id=2)
Factura.objects.create(cliente=cliente2, total=100.08)

# DETALLE FACTURA
cabecera = Factura.objects.get(id=1)
productos = Producto.objects.all()
for p in productos:
    detalle = DetalleFactura(factura=cabecera, producto=p, cantidad=3, precio=p.precio, subtotal=(p.precio * 3))
    detalle.save()

cabecera2 = Factura.objects.get(id=2)
for p in productos:
    detalle = DetalleFactura(factura=cabecera2, producto=p, cantidad=2, precio=p.precio, subtotal=(p.precio * 3))
    detalle.save()


# ACTUALIZAR REGISTROS
# ACTUALIZAR REGISTRTOS DE PRODUCTOS
p = Producto.objects.get(id=1)
p.precio = 100.3
p.save()
Producto.objects.filter(id=2).update(precio=1.7)
# ACTUALIZAR REGISTROS DE CLIENTES
C = Cliente.objects.get(id=1)
C.direccion = 'Av.Colon'
C.save()
Cliente.objects.filter(id=2).update(nombre='Joan Campos')
# ACTUALIZAR REGISTROS DE FACTURA
F = Factura.objects.get(id=1)
F.total = 200
F.save()
Factura.objects.filter(id=2).update(total=50)
# ACTUALIZAR REGISTROS DE DETALLEFACTURA
DF = DetalleFactura.objects.get(id=1)
DF.cantidad = 1700
DF.save()
DetalleFactura.objects.filter(id=2).update(precio=32)

# ELIMINAR REGISTROS EN LOS MODELOS
p = Producto.objects.get(id=2)
p.delete()
Producto.objects.filter(id=6).delete()

# QUERYS MODELOS
Producto.objects.all()
Cliente.objects.all()
Producto.objects.get(pk=1)
Cliente.objects.get(pk=1)
Producto.objects.filter(pk__lte=2)
Cliente.objects.exclude(pk=1)
Producto.objects.filter(id__lte=4).values('id','descripcion')

# QUERYS VARIOS MODELOS

Factura.objects.filter(cliente__nombre__icontains='Joan').values('id','cliente__nombre','total')
client = Cliente.objects.get(pk=2)
client.factura_set.all()