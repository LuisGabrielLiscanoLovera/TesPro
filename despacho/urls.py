import imp
from django.urls import path
#from .views import  CreateDespacho,Despachos

#from .views import despacho_list # ,createDespacho, get_despacho, updateDespacho, deleteDespacho

from .views import despacho_list,Despachos,deleteDespacho,operacionesList

#from .views import TasksView

urlpatterns = [
        
    #path('d/', TasksView.as_view(), name='task_list_url'),   
    #path('', Despachos.as_view(), name='despacho'),
    path('lista_operaciones/', operacionesList, name="operaciones-list"),
 #   path('despacho/create/', CreateDespacho.as_view(), name='Despacho_ajax_create'),



    #original
    path('', Despachos.as_view(), name='despacho'),
    path('list', despacho_list, name="despachos"),
    #path('create', createDespacho, name="newDespacho"),
    #path('<str:id>', get_despacho, name='get_despacho'),
    #path('update/<str:id>', updateDespacho, name="update"),
    path('delete/<str:id>/', deleteDespacho, name="delete")
]