from django.contrib import admin

# Register your models here.
from .models import Empresa,RelacionEmpresa

admin.site.register(Empresa)
admin.site.register(RelacionEmpresa)