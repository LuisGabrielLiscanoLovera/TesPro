from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('referencia-list/', views.referenciaList, name="referencia-list"),
	path('referencia-detail/<str:pk>/', views.referenciaDetail, name="referencia-detail"),
	path('referencia-create/', views.referenciaCreate, name="referencia-create"),
	path('referencia-update/<str:pk>/', views.referenciaUpdate, name="referencia-update"),
	path('referencia-delete/<str:pk>/', views.referenciaDelete, name="referencia-delete"),
]
