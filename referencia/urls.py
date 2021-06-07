from django.urls import path

from referencia.views import CreateCrudUser, CrudView, DeleteCrudUser, UpdateCrudUser,ReferenciaView

from .views import referenciaList

urlpatterns = [

	#path('', CrudView.as_view(), name='crud_ajax'),
    path('referencia-list/', referenciaList, name="referencia-list"),
    #path('', ReferenciaView.as_view(), name='crud_ajax_referencia'),
    path('ajax/crud/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
]
