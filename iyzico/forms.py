from django.forms import ModelForm

from .models import Payment


class PayForm(ModelForm):
    class Meta:
        model = Payment
        fields = ["ad", "soyad", "kart_no", "ay", "yil", "cvc",
                  "tel_no", "email", "adres", "sehir", "ulke", "para"]
