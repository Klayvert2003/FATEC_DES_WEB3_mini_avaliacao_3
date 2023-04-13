from django.shortcuts import render
from .models import Feriados
import datetime

def verificar_feriado(request):
    data_atual = datetime.date(day=14, month=5, year=2022)
    try:
        feriados = Feriados.objects.get(dia=data_atual.day, mes=data_atual.month)
        return render(request, 'verificar_feriado.html', {'feriados': feriados})
    except Feriados.DoesNotExist:
        return render(request, 'verificar_feriado.html', {'feriados': None})
