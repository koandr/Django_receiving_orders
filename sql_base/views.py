from django.shortcuts import render
from .models import Order
from telebot.sendmessage import sendTelegram
from .forms import OrderForm


def first_page(request):
    return render(request, './index.html')


def customer_data(request):
    form = OrderForm()
    executor = request.POST['executor']
    request.session['executor'] = executor
    return render(request, './customer_data.html', {'form': form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    address = request.POST['address']
    executor = request.session.get('executor', '')
    element = Order(order_name=name, order_phone=phone, order_address=address, order_executor=executor)
    element.save()
    sendTelegram(tg_name=name, tg_phone=phone, tg_address=address, tg_executor=executor)
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone,
                                                  'address': address,
                                                  'executor': executor
                                                  })
