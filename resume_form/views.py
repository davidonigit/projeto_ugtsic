from django.shortcuts import render
from .models import ResumeSubmit
from django.core.exceptions import ValidationError

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