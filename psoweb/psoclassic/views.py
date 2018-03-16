from django.shortcuts import render
from django.template import loader

def index(request):
    template = loader.get_template('psoclassic/index.html')
    context = { }
    return render(request,'psoclassic/index.html',context)
