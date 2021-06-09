from home.views import cambioEmpresa
from django.contrib import admin

# Register your models here.
from .models import Empresa,RelacionEmpresa,CambioEmpres

admin.site.register(Empresa)
admin.site.register(RelacionEmpresa)
admin.site.register(CambioEmpres)