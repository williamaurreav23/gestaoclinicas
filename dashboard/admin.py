from django.contrib import admin

# Register your models here.

from .models import Clientes
admin.site.register(Clientes)

from .models import Funcionario
admin.site.register(Funcionario)

from .models import Ativos
admin.site.register(Ativos)

from .models import Passivos
admin.site.register(Passivos)