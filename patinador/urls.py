from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('patinador-list/', views.patinadorList, name="patinador-list"),
	path('patinador-detail/<str:pk>/', views.patinadorDetail, name="patinador-detail"),
	path('patinador-create/', views.patinadorCreate, name="patinador-create"),
	path('patinador-update/<str:pk>/', views.patinadorUpdate, name="patinador-update"),
	path('patinador-delete/<str:pk>/', views.patinadorDelete, name="patinador-delete"),
]
