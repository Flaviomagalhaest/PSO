from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    return JsonResponse(json.loads(a))