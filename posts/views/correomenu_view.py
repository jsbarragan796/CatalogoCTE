# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from posts.forms import numeroCorreoForm
from django.contrib import messages
from posts.models import *
from .borradores_view import *
from django.core.mail import EmailMultiAlternatives
from decouple import config
from django.template.loader import render_to_string


def notification(request):
    if request.user.is_authenticated() and request.user.perfil.role == 1:
        config = CorreoConfiguracion.objects.all()
        leng = len(config)
        context = {'config': config, 'leng':leng}
        return render(request, 'notificaciones.html', context)



def number_correo_create(request):
    if request.method == 'POST':
        form = numeroCorreoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            number = cleaned_data.get('numeroCorreo')
            date = 'No se han mandado correos'
            pending = len(Herramienta.objects.all().filter(estado=1))
            correoConfig = CorreoConfiguracion.objects.create(limit=number, lastSend=date, pending=pending)
            correoConfig.save()
            messages.success(request, 'Se ha  configurado con éxito '+number+' como el limite de revisiones para'+
                             ' enviar recordatorio a los miembros conectate.',
                             extra_tags='alert alert-success')
            return redirect(reverse('catalogo:notificaciones'))
    else:
        form = numeroCorreoForm()
    return render(request, 'notificaciones_create.html', {'form': form})


def number_correo_update(request, pk):
    correoConfig = CorreoConfiguracion.objects.get(id=pk)
    if request.method == 'POST':
        form = numeroCorreoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            number = cleaned_data.get('numeroCorreo')
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            correoConfig.limit = number
            correoConfig.lastSend = date
            correoConfig.save()
            messages.success(request, 'Se ha actualizado con éxito '+str(number)+' como el limite de revisiones para'+
                             ' enviar recordatorio a los miembros conectate.',
                             extra_tags='alert alert-success')
            return redirect(reverse('catalogo:notificaciones'))
    else:
        form = numeroCorreoForm(instance=correoConfig)
    return render(request, 'notificacion_update.html', {'form': form})


def add_pending():
    correoConfigAll = CorreoConfiguracion.objects.all()
    if len(correoConfigAll) >0 :
        pk = correoConfigAll[0].id
        correoConfig = CorreoConfiguracion.objects.get(id=pk)
        correoConfig.pending = correoConfig.pending + 1
        envio = check_send_correo(correoConfig.pending, correoConfig.limit)
        if envio:
            correoConfig.lastSend = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        correoConfig.save()

def reduce_pending():
    correoConfigAll = CorreoConfiguracion.objects.all()
    if len(correoConfigAll) > 0:
        pk = correoConfigAll[0].id
        correoConfig = CorreoConfiguracion.objects.get(id=pk)
        correoConfig.pending = correoConfig.pending - 1
        correoConfig.save()


def check_send_correo (pending, limit):
    if pending >= limit :
        usuarios = User.objects.all()
        for usuario in usuarios:
            subject = 'Revisiones elementos del Catálogo'
            to_email = usuario.email
            # text_content = 'De parte del Catálogo Conecta-te le recordamos lo importante que es mantener la " \
            #                "gestion del conocimiento en sin acumulación de elementos por revision. \n" \
            #                "Le recordamos que es su responsabilidad revisar las herramientas o actividades." \

            html_content = render_to_string('email.html')         
            msg = EmailMultiAlternatives(str(subject), str('prueba 01'), config('EMAIL_HOST_USER', default=''), [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        return True
    else:
        return False

