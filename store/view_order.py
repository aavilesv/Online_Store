
from Online_Store.funciones import addUserData
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction ,IntegrityError
import datetime
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from store.models import Order,Order_detail,Customer,Product
@login_required(login_url='/seguridad/login/')
def order(request):
    data ={
        'titulo':'Consult',
        'model': 'Order',
        'ruta':'/store/order/',
        'user': request.user.username,
    }
    addUserData(request, data)
    if 'action' in request.GET:
        action = request.GET['action']
        data['action'] = action
        if action == 'cargaventa':
            try:
                with transaction.atomic():
                    ventajson = json.loads(request.GET['venta'])

                    vent = Order()
                    vent.customer = Customer.objects.get(pk=int(ventajson['cliente']))
                    vent.order_date=datetime.datetime.now()
                    vent.save()
                    for item in ventajson['items']:
                        if Product.objects.filter(id=int(item['id'])).exists():
                            detalle = Order_detail()
                            detalle.order,detalle.product = vent, Product.objects.get(pk=int(item['id']))
                            detalle.quantity,detalle.unit_price  =int(item['cantidad']), float(item['precio'])
                            detalle.total_price = round(float(item['precio'])*int(item['cantidad']))
                            detalle.save()

                    return HttpResponse(json.dumps({"resp": True}), content_type="application/json")
            except IntegrityError as ex:

                return HttpResponse(json.dumps({"resp": False, "mensaje": str(ex)}),
                                    content_type="application/json")
        if action == 'add':
            data['cliente'] = Customer.objects.all()
            data['articul'] = Product.objects.all()
            data['fecha'] = datetime.date.today()
            return render(request, 'venta/venta_form.html', data)

        if action == 'ver':
            id = request.GET['id']
            v = Order.objects.get(pk=int(id))
            data['venta'], data['detalle'] = v, Order_detail.objects.filter(order=Order.objects.get(pk=int(id)))

            return render(request, 'venta/venta_visualizar.html', data)

    else:
        # Viaja por get
        data['venta'] =  Order.objects.all().order_by('id')
        return render(request, 'venta/Venta.html', data)
