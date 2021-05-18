from django.urls import path
from .views import *

urlpatterns = [


    path('',ReferenciaView.as_view(), name='Referencia_ajax'),
    path('ajax/Referencia/create/', CreateReferenciaUser.as_view(), name='Referencia_ajax_create'),
    path('ajax/Referencia/delete/', DeleteReferenciaUser.as_view(), name='Referencia_ajax_delete'),
    path('ajax/Referencia/update/', UpdateReferenciaUser.as_view(), name='Referencia_ajax_update'),
	
  	#path('', views.apiOverview, name="referenciaHome"),
	#path('referencia-list/', views.referenciaList, name="referencia-list"),
	# path('referencia-detail/<str:pk>/', views.referenciaDetail, name="referencia-detail"),
	# path('referencia-create/', views.referenciaCreate, name="referencia-create"),
	# path('referencia-update/<str:pk>/', views.referenciaUpdate, name="referencia-update"),
	# path('referencia-delete/<str:pk>/', views.referenciaDelete, name="referencia-delete"),
]
