from django.contrib import admin

# Register your models here.

from .models import Clientes
admin.site.register(Clientes)

from .models import Gestor
admin.site.register(Gestor)