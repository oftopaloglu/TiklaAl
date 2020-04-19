from django.db import models 

class Payment(models.Model):
    ad = models.CharField(max_length=50, null=True, verbose_name="Ad")
    soyad = models.CharField(max_length=50, null=True, verbose_name="Soyad")
    kart_no = models.CharField(max_length=50, null=True, verbose_name="Kart No")
    ay = models.CharField(max_length=50, null=True, verbose_name="Ay")
    yil = models.CharField(max_length=50, null=True, verbose_name="Yıl")
    cvc = models.CharField(max_length=50, null=True, verbose_name="CVC")
    tel_no = models.CharField(max_length=50, null=True, verbose_name="Telefon No")
    email = models.CharField(max_length=50, null=True, verbose_name="E-Posta")
    adres = models.CharField(max_length=50, null=True, verbose_name="Adres")
    sehir = models.CharField(max_length=50, null=True, verbose_name="Şehir")
    ulke = models.CharField(max_length=50, null=True, verbose_name="Ülke")
    tarih = models.DateTimeField("Tarih", null=True, auto_now=True)
    para = models.IntegerField(null=True)
    def __str__(self):
        return self.ad

class TotalPrice(models.Model):
    kullanici = models.ForeignKey("auth.user", on_delete=models.CASCADE, verbose_name="Kullanıcı")
    toplam_para = models.IntegerField()
