from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import contactForm

# Create your views here.

def contact(request):
    contact_form = contactForm()
    if request.method== "POST":
        contact_form = contactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            mensaje = request.POST.get('mensaje', '')
            #enviamos el correo y redireccionamiento
            email= EmailMessage(
                "Programador: nuevo mensaje de contacto",
                "de {} <{}>\n\nEscribio:\n\n{}".format(name, email, mensaje), 
                "no-contestar@inbox.mailtrap.io",
                ["adrianhenao994@gmail.com"],
                reply_to=[email]
            )
            
            try:
                email.send()
                #codigo correcto
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien 
                return redirect(reverse('contact')+"?fail")
        
    return render(request, "contact/contact.html", {"form": contact_form})