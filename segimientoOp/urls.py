from django.urls import path
from .views import SegimientoOp
from django.conf.urls import url

urlpatterns = [
    
    url(r'^SegimientoOp$', SegimientoOp.as_view(), name='SegimientoOp'),   
]