from django.shortcuts import render
from .models import Feriados
import datetime

def verificar_feriado(request):
    data_atual = datetime.date.today()
    #data_atual = datetime.date(day=25, month=12, year=2022)
    try:
        feriados = Feriados.objects.get(dia=data_atual.day, mes=data_atual.month)
        return render(request, 'verificar_feriado.html', {'feriados': feriados})
    except Feriados.DoesNotExist:
        return render(request, 'verificar_feriado.html', {'feriados': None})
