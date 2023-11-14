from django.shortcuts import render


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    address = request.POST['address']
    print(type(address))
#    element = Order(order_name=name, order_phone=phone, order_address=address)
#    element.save()
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone,
                                                  'address': address
                                                  })


print("QWERTY")