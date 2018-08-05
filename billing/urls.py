from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^showpos/',views.showpos,name='showpos'),
    url(r'^invoice-list/$', views.invoices, name='invoices'),


    ]
