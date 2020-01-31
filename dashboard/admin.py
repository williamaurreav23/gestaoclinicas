from .models import Funcionario
from django.contrib import admin

# Register your models here.

from .models import Clientes
admin.site.register(Clientes)

admin.site.register(Funcionario)
