from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import ResumeSubmit

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        resume = ResumeSubmit(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            celphone = request.POST.get('celphone'),
            position = request.POST.get('position'),
            education = request.POST.get('education'),
            observations = request.POST.get('observations'),
            file = request.FILES.get('file'),
            ip = get_client_ip(request),
        )
        try:
            resume.full_clean()
            resume.save()

            subject='Confirmação de Submissão do Currículo'
            message=f'''Olá {resume.name},
Confirmamos o recebimento da sua aplicação para a posição de {resume.position}.
            
Dados enviados:
Nome: {resume.name}
Email: {resume.email}
Telefone: {resume.celphone}
Cargo: {resume.position}
Escolaridade: {resume.education}
Observações: {resume.observations}

Segue o currículo em anexo.
'''
            recipient_list=[resume.email]

            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipient_list
            )
            email.attach(resume.file.name, resume.file.read())
            email.send(fail_silently=False)

            return render(request, 'submit_success.html')
        except ValidationError as e:
            return render(request, 'home.html', {'errors': e.message_dict})  

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip