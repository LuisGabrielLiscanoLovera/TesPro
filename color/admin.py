from django.contrib import admin

# Register your models here.
from .models import Color
from .models import Todo

# Register your models here.

admin.site.register(Todo)
admin.site.register(Color)