from .IndivClass import Individuo
from json import dumps
gbest = ''
config = { 'nrIteracoes' : 100 }

def execute(pontos,objetivo, const):
    #Transformando os pontos recebidos em individuos. Guardando numa lista
    #Calculando valor de fitness em seu construtor
    indivs = []
    for ponto in pontos:
        indivs.append(Individuo(ponto, objetivo))
    #Identificando gbest
    gbest = defineGbest(indivs)
    
    #Calculando velocidade dos eixos x e y. Atualizando posicao
    for indiv in indivs:
        indiv.calcVelocidade('x',const,gbest)
        indiv.calcVelocidade('y',const,gbest)
        
        #Atualizando posicao
        indiv.atual['x'] += indiv.velocidade['x']
        indiv.atual['y'] += indiv.velocidade['y']
    
    return SerializarObjJSON(indivs)


def iteracao(objetivo,gbest,indivs):
    pass
    
#calcula gbest
def defineGbest(indivs):
    return min(indivs, key=lambda x:x.fitnessAtual)

#Transforma objeto com individuos em uma String com apenas posicao atual
def SerializarObjJSON(indivs):
    json = []
    for indiv in indivs:
        jsonIndiv = dict(indiv.atual)
        json.append(jsonIndiv)
    return dumps(json)