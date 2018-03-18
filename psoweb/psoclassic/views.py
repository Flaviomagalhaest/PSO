from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from py import classico
from py.classico import PSOClassic as pso
import json

def index(request):
    template = loader.get_template('psoclassic/index.html')
    context = { }
    return render(request,'psoclassic/index.html',context)

@csrf_exempt
def calcula(request):
    jsonAjax = request.body
    data = json.loads(jsonAjax)
    indiv = json.loads(data['indiv'])
    objetivo = json.loads(data['objetivo'])
    constantes = json.loads(data['constantes'])
    indivs = pso.execute(indiv,objetivo,constantes)
    return JsonResponse(json.loads(indivs), safe=False)