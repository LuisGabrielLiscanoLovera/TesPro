from django.urls import path

from color.views import CreateColor,DeleteColor,UpdateColor
from .views import colorList

urlpatterns = [

    path('color-list/', colorList, name="color-list"),
    path('color/crud/create/', CreateColor.as_view(), name='Color_ajax_create'),
    path('color/crud/delete/', DeleteColor.as_view(), name='Color_ajax_delete'),
    path('color/crud/Update/', UpdateColor.as_view(), name='Color_ajax_update'),
   
]
