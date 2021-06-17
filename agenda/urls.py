from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'agenda'

urlpatterns = [
    path('', RedirectView.as_view(url='/agenda/')),
    path('agenda/', views.lista_eventos, name='lista_eventos'),
    path('agenda/eventos/finalizado/', views.lista_eventos_finalizados, name='eventos_finalizados'),
    path('agenda/lista/', views.json_lista_evento, name='json_lista_evento'),
    
    path('agenda/evento/', views.evento, name='agenda_evento'),
    path('agenda/evento/submit', views.submit_evento, name='submit_evento'),
    path('agenda/evento/delete/<int:id_evento>', views.delete_evento, name='delete_evento'),
    
    path('login/', views.login_user, name='login_user'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('logout/', views.logout_user, name='logout_user'),
]