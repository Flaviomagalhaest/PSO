from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import assembler as assembler
from py.tsp import tspController as tspController
import json, os

def index(request):
    template = loader.get_template('PSO-tsp/index.html')
    #Lê arquivos txt de problemas padrão que se encontram na pasta
    arquivos = os.listdir('PSO-tsp/static/PSO-tsp/file')
    context = { 'arquivos' : arquivos }
    return render(request,'PSO-tsp/index.html',context)

@csrf_exempt
def calcMatrixDist(request):
    jsonAjax = request.body
    
    #Pontos iniciais vindo do frontend.
    data = json.loads(jsonAjax)     
    
    #Alimentando lista de pontos. Por arquivo ou pelos pontos passados do front.
    #Se TRUE, Os pontos serão importados pelo arquivo txt.
    #Se FALSE, Os pontos serão usados pelos que foram passados pelo front
    if data['usarArquivo'] == True: 
        pontosJson = assembler.lerArquivoDePontos(data["nomeDoArquivo"], data["width"], data["height"])
    else:   
        pontosJson = json.loads(data['pontos']) #Transformando em json.
    
    #Chamando controller que instanciará objeto de pontos e calculará matriz distância.
    pontosObj = tspController.calcMatrixDist(pontosJson)    
    
    #Salvando informações de pontos em formato JSON em sessão.
    request.session['pontos'] = pontosObj.toJson()
    request.session['qtdPontos'] = len(pontosObj.pontos)

    return JsonResponse(request.session['pontos'], safe=False)

@csrf_exempt
def geraPopInicial(request):

    #Recebendo quantidade de indivíduos a criar.
    jsonAjax = json.loads(request.body)
    
    qtdIndiv = json.loads(jsonAjax['individuos'])
    qtdPontos = request.session['qtdPontos']
    pontosSessao = request.session['pontos']

    #Gerando individuos iniciais
    individuos = tspController.geraPopInicial(qtdIndiv, qtdPontos, pontosSessao)
    
    #Criando lista de individuo em formato serializável em json
    individuosJson = [i.toJson() for i in individuos]   
    
    #Salvando individuos em sessão
    request.session['individuos'] = individuosJson
    return JsonResponse(individuosJson, safe=False)

@csrf_exempt
def geraIteracao(request):
    jsonAjax = json.loads(request.body) #Recebendo numero de iteracao atual e a quantidade a calcular
    iteracaoAtual = jsonAjax['iteracaoAtual']
    nrIteracoes = jsonAjax['nrIteracoes']
    individuosJson = request.session['individuos']  #Buscando individuos na sessao
    pontosSessao = request.session['pontos']        #Buscando pontos na sessao
    #Gerando iteracoes e atualizando individuos
    individuos = tspController.geraIteracao(iteracaoAtual, nrIteracoes, individuosJson, pontosSessao)
    individuosJson = [i.toJson() for i in individuos]   #Criando lista de individuo em formato serializável em json
    request.session['individuos'] = individuosJson    #Salvando individuos em sessão
    return JsonResponse(individuosJson, safe=False)


@csrf_exempt
def teste(request):
    context = { }
    return render(request,'PSO-tsp/index.html',context)


