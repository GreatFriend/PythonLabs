from django.shortcuts import render
from .models import Citizen
from .forms import *

def index(request):
    citizens = Citizen.objects.all()
    return render(request, 'lab/index.html', {'citizens': citizens})

def detail(request, id_):
    citizens = Citizen.objects.get(pk=id_)
    return render(request, 'lab/detail.html', {'citizens': citizens})

def add(request):
    form=Form(request.POST or None)
    if request.method=='GET':
        context= {'form':form}
        return render(request,'lab/add.html',context)
    else:      
        if form.is_valid():
            form.save()
            citizens = Citizen.objects.all()
            return render(request, 'lab/index.html', {'citizens': citizens})
        else:
            return render(request,'lab/add.html',{'form':form})

def update(request, id_):
    form=Form(request.POST or None,instance=Citizen.objects.get(pk=id_))
    if request.method=='GET':
        return render(request,'lab/update.html',{'form':form,'citizen':Citizen.objects.get(pk=id_)})
    else:      
        if form.is_valid():
            form.save()
            citizens = Citizen.objects.all()
            return render(request, 'lab/index.html', {'citizens': citizens})
        else:
            return render(request,'lab/update.html',{'form':form,'citizen':Citizen.objects.get(pk=id_)})


def remove(request, id_):
    citizens = Citizen.objects.get(pk=id_)
    citizens.delete()
    citizens = Citizen.objects.all()
    return render(request, 'lab/index.html', {'citizens': citizens})

