from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('prenda-list/', views.prendaList, name="prenda-list"),
	path('prenda-detail/<str:pk>/', views.prendaDetail, name="prenda-detail"),
	path('prenda-create/', views.prendaCreate, name="prenda-create"),
	path('prenda-update/<str:pk>/', views.prendaUpdate, name="prenda-update"),
	path('prenda-delete/<str:pk>/', views.prendaDelete, name="prenda-delete"),
]
