from django.shortcuts import render
from django.template import loader
from py import ConfigConstants as cc
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('googlemapspso/index.html')
    key = cc.inicializaConfig()
    #context=RequestContext(request)
    #context['key'] = key.key
    context = {
        'key': key.key
    }
    return render(request,'googlemapspso/index.html',context)
    #return HttpResponse(template.render(context,request))


@csrf_exempt 
def teste(request):
    a = 1