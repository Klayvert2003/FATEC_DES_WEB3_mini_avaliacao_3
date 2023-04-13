from django.db import models

class Feriados(models.Model):
    nome = models.CharField('Feriados', max_length=50)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mês')
    modificado_em = models.DateTimeField(verbose_name='modificado em', auto_now_add=False, auto_now=True)

    # Executar no terminal:
    # python manage.py shell

    # from core.models import Feriados
    # Feriados.objects.create(nome='Natal', dia=25, mes=12)
    # Feriados.objects.create(nome='Tiradentes', dia=21, mes=4)
    # Feriados.objects.create(nome='Dia Das Mães', dia=14, mes=5)

    def __str__(self):
        return self.nome