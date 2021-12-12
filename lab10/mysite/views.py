from django.shortcuts import render
from lab.models import Citizen


def index(request):
    citizens = Citizen.objects.all()
    return render(request, 'lab/index.html', {'citizens': citizens})

