from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contexto = {}
    if request.method == 'POST':
        fomulario = ContactForm(request.POST)
        if fomulario.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

            email = EmailMessage(
                'Mensaje de contacto recibido',
                f'Mensaje enviado por {name} <{email}> telefono<{phone}>:\n\nAsunto:{subject}\n\n{message}',
                email,
                ['f39dceba809abd@inbox.mailtrap.io'],
                reply_to=[email],
            )
            try:
                email.send()
                # Está todo OK
                messages.add_message(request, messages.SUCCESS, 'El mensaje se ha enviado correctamente!', extra_tags='success')
                return redirect(reverse('contacto')+'?ok')
            except Exception as e:
                # Ha habido un error y retorno a ERROR
                print(e)
                messages.add_message(request, messages.ERROR, 'Ocurrio un error, intente nuevamente mas tarde', extra_tags='danger')
                return redirect(reverse('contacto')+'?error')

        else:
            messages.add_message(request, messages.ERROR, '¡Uno o mas campos no están ingresados correctamente!', extra_tags='danger')
    else:
        fomulario = ContactForm()
    
    contexto = {
        'contact_form':fomulario
    }
    
    return render(request, 'contact/contact.html', contexto)
