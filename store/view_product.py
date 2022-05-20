from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Online_Store.funciones import addUserData
from django.db import transaction
from django.shortcuts import render, redirect
from store.models import Product
@login_required(login_url='/seguridad/login/')
def product(request):
    data ={
        'titulo':'Consulta de Product',
        'model': 'Product',
        'ruta':'/store/product/',
        'user': request.user.username,
    }
    addUserData(request, data)
    if request.method == 'POST':
        if 'action' in request.POST:
            action = request.POST['action']
            try:
                with transaction.atomic():
                    if action == 'add':
                        articulo =Product()
                        articulo.name, articulo.price = request.POST['name'], request.POST['price']
                        articulo.create=(request.POST['create_date'])
                        articulo.save()
                    if action == 'edit':
                        articulo = Product.objects.select_related().get(pk=request.POST['id'])
                        articulo.name, articulo.price = request.POST['name'], request.POST['price']
                        articulo.create = (request.POST['create_date'])
                        articulo.save()
            except Exception as ex:
                messages.error(request, str(ex))
            return redirect('/store/product/')
    else:
        if 'action' in request.GET:
            if (request.GET['action'] == 'add'):
                data['action'], data['id'] = request.GET['action'], request.GET['id']
                return render(request, 'inventario/articulo_modal.html', data)

            if (request.GET['action'] == 'edit'):
                data['action'], data['id'] = request.GET['action'], request.GET['id']
                data['articulo'] = Product.objects.get(id=request.GET['id'])
                return render(request, 'inventario/articulo_modal.html', data)
        data['articulo'] = Product.objects.all()
        return  render(request, 'inventario/articulo.html', data)
