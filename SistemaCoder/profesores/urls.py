from django.urls import path
from . import views


app_name = 'profesor'
urlpatterns = [
    path('', views.index, name='index' ),
    path('formulario', views.formulario, name="formulario"),
    path(
        '<int:profesor_id>', 
        views.detalle,
        name='detalle' )
]
