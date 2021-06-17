from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from agenda.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta


def login_user(request):
    return render(request, 'accounts/login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if username and password:
            
            if usuario is not None:
                login(request, usuario)
                return redirect('/')
            else:
                messages.error(request, 'usuario ou senha invalido.')
        else:
            messages.error(request, 'usuario ou senha não inserido')
    
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

# def index(request):
#     return redirect('/agenda/')

@login_required(login_url='/login/')
def lista_eventos(request):
    context = {}
    usuario = request.user
    data_atual = datetime.now() - timedelta(days=2)
    finalizado = 1
    context['eventos'] = Evento.objects.filter(usuario=usuario).exclude(status=finalizado).order_by('data_criacao').reverse()
    # context['eventos'] = Evento.objects.filter(usuario=usuario, data_evento__gte=data_atual).order_by('data_criacao').reverse()    
    return render(request, 'agenda/dashboard.html', context)


@login_required(login_url='/login/')
def lista_eventos_finalizados(request):
    context = {}
    usuario = request.user 
    finalizado = 1
    context['eventos'] = Evento.objects.filter(usuario=usuario, status=finalizado).order_by('data_criacao').reverse()
    return render(request, 'agenda/eventos_finalizados.html', context)


@login_required(login_url='/login/')
def json_lista_evento(request):
    id_evento = request.GET.get('id')
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario, id=id_evento).order_by('data_criacao').reverse().values('id', 'titulo', 'data_criacao', 'data_evento', 'status')
            
    return JsonResponse(list(evento), safe=False)


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    context = {}
    if id_evento:
        context['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'agenda/evento.html', context)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        id_evento = request.POST.get('id_evento')
        titulo = request.POST.get('evento')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        status = request.POST.get('status')
        usuario = request.user
        if id_evento: # se for atualiziação entra neste IF
            # Evento.objects.filter(id=id_evento).update(titulo=titulo, descricao=descricao, data_evento=data_evento, usuario=usuario, status=status)
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao 
                evento.data_evento = data_evento
                evento.status = status
                evento.save()
            messages.success(request, f'Evento {titulo} atuliazado com sucesso. ')
            
        else:
            if titulo and descricao and data_evento:
                Evento.objects.create(titulo=titulo, descricao=descricao, data_evento=data_evento, usuario=usuario)
            else:
                messages.error(request, 'Preencha todos os campos.')
                return render(request, 'agenda/evento.html')
    
    
    return redirect('/')
    
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
        messages.success(request, f'Evento {evento.titulo} deletado com sucesso.')
    else:
        messages.error(request, f'Erro ao tentar deletar evento {evento.titulo}')
    return redirect('/')