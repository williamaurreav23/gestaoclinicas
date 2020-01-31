from .models import Rentabilidade
from .models import Passivos
from django.contrib import admin

# Register your models here.
from .models import Ativos
admin.site.register(Ativos)

admin.site.register(Passivos)

admin.site.register(Rentabilidade)
