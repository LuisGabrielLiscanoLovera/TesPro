from django.urls import path

from referencia.views import CreateReferencia,DeleteReferencia,UpdateReferencia, CrudView, DeleteCrudUser, UpdateCrudUser,ReferenciaView,CreateCrudUser

from .views import referenciaList

urlpatterns = [

	#path('', CrudView.as_view(), name='crud_ajax'),
    path('referencia-list/', referenciaList, name="referencia-list"),
    path('referencia/crud/create/', CreateReferencia.as_view(), name='Referencia_ajax_create'),
    path('referencia/crud/delete/', DeleteReferencia.as_view(), name='Referencia_ajax_delete'),
    path('referencia/crud/Update/', UpdateReferencia.as_view(), name='Referencia_ajax_update'),
    path('ajax/crud/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
]
