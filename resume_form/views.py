from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import ResumeSubmit
from .forms import ResumeForm

def home(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        
        if form.is_valid():
            resume = form.save(commit=False)
            resume.ip = get_client_ip(request)
            resume.save()

            subject = 'Confirmação de Submissão do Currículo'
            message = f'''Olá {resume.name},
Confirmamos o recebimento da sua aplicação para a posição de {resume.position}.
            
Dados enviados:
Nome: {resume.name}
Email: {resume.email}
Telefone: {resume.phone}
Cargo: {resume.position}
Escolaridade: {resume.get_education_display()}
Observações: {resume.observations}

Segue o currículo em anexo.
'''
            recipient_list = [resume.email]

            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipient_list
            )
            email.attach(resume.file.name, resume.file.read())
            email.send(fail_silently=False)

            return render(request, 'submit_success.html')
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = ResumeForm()
    
    return render(request, 'home.html', {'form': form})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip