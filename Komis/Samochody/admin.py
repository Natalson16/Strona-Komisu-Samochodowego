from django.contrib import admin
from .models import Samochod, Marka, Model

# Register your models here.
admin.site.register(Samochod)
admin.site.register(Marka)
admin.site.register(Model)
