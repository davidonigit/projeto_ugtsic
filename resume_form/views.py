from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume
from django.core.exceptions import ValidationError


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        resume = Resume(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            celphone = request.POST.get('celphone'),
            position = request.POST.get('position'),
            education = request.POST.get('education'),
            observations = request.POST.get('observations'),
            file = request.FILES.get('file')
        )

        try:
            resume.full_clean()
            resume.save()
            return render(request, 'submit_success.html')
        except ValidationError as e:
            return render(request, 'home.html', {'errors': e.message_dict})