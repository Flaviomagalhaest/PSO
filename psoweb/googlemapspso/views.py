from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from py import ConfigConstants as cc

def index(request):
    template = loader.get_template('googlemapspso/index.html')
    key = cc.inicializaConfig()
    context = {
        'key': key.key
    }
    return HttpResponse(template.render(context,request))
