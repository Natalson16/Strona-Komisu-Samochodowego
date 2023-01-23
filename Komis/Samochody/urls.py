from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('marka/<id>/', views.marka, name="marka"),
    path('model/<id>/', views.model, name="model"),
    path('samochod/<id>/', views.samochod, name="samochod"),

    path('rejestracja/', views.registerPage, name="rejestracja"),
    path('logowanie/', views.loginPage, name="logowanie"),
    path('wylogowanie/', views.logoutUser, name="wylogowanie")
]
