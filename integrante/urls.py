from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('integrante-list/', views.integranteList, name="integrante-list"),
	path('integrante-detail/<str:pk>/', views.integranteDetail, name="integrante-detail"),
	path('integrante-create/', views.integranteCreate, name="integrante-create"),
	path('integrante-update/<str:pk>/', views.integranteUpdate, name="integrante-update"),
	path('integrante-delete/<str:pk>/', views.integranteDelete, name="integrante-delete"),
]
