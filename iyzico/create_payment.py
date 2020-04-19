# import sqlite3
import iyzipay
import json

from .data import veri
# db = sqlite3.connect("db.sqlite3")

# vt = db.cursor()

# oku = vt.execute("SELECT * from iyzico_payment")
# veri = oku.fetchall()[-1]

# vt.close()

options = {
    'api_key': "sandbox-xMmsty6A68us9iGfhLxIm7UVQ4WRSlQy",
    'secret_key': "sandbox-QQnp3eC4j2kYe5nCS0nogK4H0gCau9HH",
    'base_url': iyzipay.base_url
}



payment_card = veri

buyer = veri

address = veri

basket_items = veri

request = veri


def ode():

    payment = iyzipay.Payment().create(request, options)

    ode = payment.read().decode('utf-8')
    dic = json.loads(ode)
    print(dic)

    return dic["status"]



    


