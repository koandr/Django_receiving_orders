from django.shortcuts import render
from .models import Order
from telebot.sendmessage import sendTelegram

# Create your views here.


def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    address = request.POST['address']
    element = Order(order_name=name, order_phone=phone, order_address=address)
    element.save()
    sendTelegram(tg_name=name, tg_phone=phone)
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone,
                                                  'address': address
                                                  })
