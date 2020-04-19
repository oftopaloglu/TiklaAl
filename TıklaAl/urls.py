from django.contrib import admin
from django.urls import path

from user.views import index, loginUser
from iyzico.views import pay, detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login.html', loginUser),
    path('pay.html', pay, name="pay"),
    path('detail.html', detail, name="detail"),
]
