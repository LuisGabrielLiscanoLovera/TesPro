from django.contrib import admin

# Register your models here.
from .models import Talla,CanTalla
admin.site.register(Talla)
admin.site.register(CanTalla)