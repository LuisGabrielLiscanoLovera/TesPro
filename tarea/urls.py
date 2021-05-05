from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('tarea-list/', views.tareaList, name="tarea-list"),
	path('tarea-detail/<str:pk>/', views.tareaDetail, name="tarea-detail"),
	path('tarea-create/', views.tareaCreate, name="tarea-create"),
	path('tarea-update/<str:pk>/', views.tareaUpdate, name="tarea-update"),
	path('tarea-delete/<str:pk>/', views.tareaDelete, name="tarea-delete"),
]
