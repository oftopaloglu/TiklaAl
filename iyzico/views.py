import iyzipay
import sqlite3
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PayForm

# from . import total_price
# from . import create_payment


@login_required(login_url="/")
def pay(request):
    form = PayForm(request.POST or None)
    context = {
        "form": form
    }


    if form.is_valid():
        print(form.cleaned_data)

        ad = form.cleaned_data.get("ad")
        soyad = form.cleaned_data.get("soyad")
        kart_no = form.cleaned_data.get("kart_no")
        ay = form.cleaned_data.get("ay")
        yil = form.cleaned_data.get("yil")
        cvc = form.cleaned_data.get("cvc")
        tel_no = form.cleaned_data.get("tel_no")
        email = form.cleaned_data.get("email")
        adres = form.cleaned_data.get("adres")
        sehir = form.cleaned_data.get("sehir")
        ulke = form.cleaned_data.get("ulke")
        para = form.cleaned_data.get("para")

        options = {
        'api_key': "sandbox-xMmsty6A68us9iGfhLxIm7UVQ4WRSlQy",
        'secret_key': "sandbox-QQnp3eC4j2kYe5nCS0nogK4H0gCau9HH",
        'base_url': iyzipay.base_url
        }

        kart = {
            'cardHolderName': ad+" "+soyad,
            'cardNumber': kart_no,
            'expireMonth': ay,
            'expireYear': yil,
            'cvc': cvc,
            'registerCard': '0'
        }

        alici = {
            'id': 'BY789',
            'name': ad,
            'surname': soyad,
            'gsmNumber': tel_no,
            'email': email,
            'identityNumber': '74300864791',
            'lastLoginDate': '2015-10-05 12:43:35',
            'registrationDate': '2013-04-21 15:12:09',
            'registrationAddress': adres,
            'ip': '85.34.78.112',
            'city': sehir,
            'country': ulke,
            'zipCode': '34732'
        }

        adres = {
            'contactName': ad+" "+soyad,
            'city': sehir,
            'country': ulke,
            'address': adres,
            'zipCode': '34732'
        }

        sepet = [
            {
                'id': 'BI101',
                'name': 'Kalem',
                'category1': 'Kırtasiye',
                'category2': 'Ofis',
                'itemType': 'PHYSICAL',
                'price': para
            }
        ]

        istek = {
            'locale': 'tr',
            'conversationId': '123456789',
            'price': para,
            'paidPrice': para,
            'currency': 'TRY',
            'installment': '1',
            'basketId': 'B67832',
            'paymentChannel': 'WEB',
            'paymentGroup': 'PRODUCT',
            'paymentCard': kart,
            'buyer': alici,
            'shippingAddress': adres,
            'billingAddress': adres,
            'basketItems': sepet
        }

        payment_card = kart

        buyer = alici

        address = adres

        basket_items = sepet

        request = istek

        payment = iyzipay.Payment().create(request, options)

        ode = payment.read().decode('utf-8')
        dic = json.loads(ode)
        print(dic)

        if dic["status"] == "success":
            form.save()
        
        return redirect("detail")

    return render(request, "pay.html", context)
 

@login_required(login_url="/")
def detail(request):
    db = sqlite3.connect("db.sqlite3")

    vt = db.cursor()

    read = vt.execute("SELECT para from iyzico_payment")

    sum = 0

    for price in read:
        price = str(price)
        price = int(price[1:-2])
        
        sum += price
        
    vt.close()

    veri = sum
    
    context = {
        "veri": veri
    }
    return render(request, "detail.html", context)
