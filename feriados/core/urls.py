from django.urls import path
from .views import verificar_feriado

urlpatterns = [
    path('', verificar_feriado, name='verificar_feriado'),
]
