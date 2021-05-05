from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('casino-list/', views.casinoList, name="casino-list"),
	path('casino-detail/<str:pk>/', views.casinoDetail, name="casino-detail"),
	path('casino-create/', views.casinoCreate, name="casino-create"),
	path('casino-update/<str:pk>/', views.casinoUpdate, name="casino-update"),
	path('casino-delete/<str:pk>/', views.casinoDelete, name="casino-delete"),
]
