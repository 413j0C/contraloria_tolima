from django.urls import path
from .views import registrar_activo, formulario

urlpatterns = [
    path('activo/', registrar_activo, name='activo'),
    path('formulario/<int:pk>/', formulario, name='formulario'),
]
