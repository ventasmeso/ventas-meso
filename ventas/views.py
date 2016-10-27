from django.shortcuts import render
# Create your views here.

def listado_productos(request):
        return render(request, 'ventas/listado_productos.html', {})