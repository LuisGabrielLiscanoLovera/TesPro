from django.urls import path
from tarea.views import CreateTarea,DeleteTarea,UpdateTarea,TareaList

urlpatterns = [
    path('tarea-list/', TareaList, name="tarea-list"),
    path('tarea/crud/create/', CreateTarea.as_view(), name='Tarea_ajax_create'),
    path('tarea/crud/update/', UpdateTarea.as_view(), name='Tarea_ajax_update'),
    path('tarea/crud/delete/', DeleteTarea.as_view(), name='Tarea_ajax_delete'),


]
