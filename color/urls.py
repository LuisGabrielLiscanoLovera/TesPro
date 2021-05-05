from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('color-list/', views.colorList, name="color-list"),
	path('color-detail/<str:pk>/', views.colorDetail, name="color-detail"),
	path('color-create/', views.colorCreate, name="color-create"),
	path('color-update/<str:pk>/', views.colorUpdate, name="color-update"),
	path('color-delete/<str:pk>/', views.colorDelete, name="color-delete"),
]
