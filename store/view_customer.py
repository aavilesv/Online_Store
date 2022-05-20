from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Online_Store.funciones import addUserData
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from store.models import Customer


@login_required(login_url='/seguridad/login/')
def customer(request):
    data ={
        'titulo':'Consult',
        'model': 'Cliente',
        'ruta':'/store/Customer/',
        'user': request.user.username,
    }
    addUserData(request, data)
    segurid=User.groups.through.objects.get(user_id=request.user.id)

    if segurid.group.name == 'Empleado':
        return redirect('/seguridad/login/')
    if request.method == 'POST':
        if 'action' in request.POST:
            action = request.POST['action']
            try:
                with transaction.atomic():
                    if action == 'add':
                        clien = Customer()
                        clien.first_name,clien.email,clien.last_name = request.POST['first_name'],request.POST['email'], request.POST['last_name']
                        clien.user, clien.identification= request.user, request.POST['identification']
                        clien.save()
                    if action == 'edit':
                        clien = Customer.objects.get(pk=int(request.POST['id']))
                        clien.first_name, clien.email, clien.last_name = request.POST['first_name'], request.POST['email'], request.POST['last_name']
                        clien.user, clien.identification = request.user, request.POST['identification']
                        clien.save()


            except Exception as ex:
                messages.error(request, str(ex))
            return redirect('/store/Customer/')
    else:
        # Por primera vez viaja por Get
        if 'action' in request.GET:

            if  request.GET['action'] == 'add':
                data['action'] = request.GET['action']
                data['id'] = request.GET['id']
                return render(request, 'venta/cliente_modal.html', data)

            elif (request.GET['action'] == 'edit'):
                data['action'], data['id'] = request.GET['action'], request.GET['id']
                data['client'] = Customer.objects.get(id=request.GET['id'])
                return render(request, 'venta/cliente_modal.html', data)
        else:
            # Viaja por get
            data['cliente'] = Customer.objects.all()
            return render(request, 'venta/cliente.html', data)
