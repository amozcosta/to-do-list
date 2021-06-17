from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Evento(models.Model):
    
    F = 1
    E = 2
    A = 3
    STATUS_EVENTO = (
        (F, 'Finalizado'),
        (E, 'Executando'),
        (A, 'Aberto')
    )
    
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1500, blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS_EVENTO, default=3)

    # class Meta:
    #     db_table = 'evento' Este campo define no banco de dados o nome da tabela, se não for inserido o django atribui nomedoapp_classe como nome da tabela

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')
    
    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M')
    
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    
    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False 