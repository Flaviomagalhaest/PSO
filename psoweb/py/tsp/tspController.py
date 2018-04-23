from py.tsp import PontosClass as P
from py.tsp import IndividuoClass as I
import random, json

def calcMatrixDist(pontosJson):
    pontosObj = P.Pontos(dictPontos = pontosJson)    #Instanciando classe de Pontos. Passando dicionario de coord.
    pontosObj.calcMatrixDist()      #Calculando para cada ponto em Pontos, sua matriz distância.
    return pontosObj

def geraPopInicial(qtdPopInicial, qtdPontos, pontosJson):
    individuos = []    #Lista de individuos.
    pontos = P.Pontos(jsonSessao=pontosJson)    #Instanciando classe pontos passando string json.
    for i in range(0,qtdPopInicial):    #Loop para criar individuos dependendo da quantidade passada.
        caminhoRandom = random.sample(range(qtdPontos),qtdPontos)   #Criando lista de numeros aleatorios (caminho).
        caminhoRandom.append(caminhoRandom[0])  #Adicionando primeiro termo no final. O caminho tem que ser ciclico.
        distanciaCaminho = pontos.calcDistDeCaminhos(caminhoRandom) #Calculando distancia.
        indiv = I.Individuo(caminhoRandom, distanciaCaminho)        #Instanciando classe Individuo passando caminho e distancia.
        individuos.append(indiv)   #Adicionando individuo instanciado na lista.
    return individuos

def geraIteracao(iteracaoAtual, nrIteracoes, individuosJson):
    individuos = []    #Lista de individuos.
    for i in range(0,len(individuosJson)): #Itera lista de individuos em Json para instanciar no objeto individuos
        individuo = I.Individuo(json=json.loads(individuosJson[i]))
        individuos.append(individuo)    #Lista de individuos já instanciados
    
    #Começando iterações
    for j in range(0,nrIteracoes):
        #Calculando constantes k e m
        k = randint(0,)   
    a = 1
