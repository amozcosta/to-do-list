from django.contrib import admin
from agenda.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao', 'status')
    list_filter = ('titulo', 'usuario', 'data_evento', 'status')

admin.site.register(Evento, EventoAdmin)