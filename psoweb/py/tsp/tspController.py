from py.tsp import PontosClass as P
from py.tsp import IndividuoClass as I
import random

def calcMatrixDist(pontosJson):
    pontosObj = P.Pontos(dictPontos = pontosJson)    #Instanciando classe de Pontos. Passando dicionario de coord.
    pontosObj.calcMatrixDist()      #Calculando para cada ponto em Pontos, sua matriz distância.
    return pontosObj

def geraPopInicial(qtdPopInicial, qtdPontos, pontosJson):
    individuos = []    #Lista de individuos.
    pontos = P.Pontos(jsonSessao=pontosJson)    #Instanciando classe pontos passando string json.
    for i in range(0,qtdPopInicial):    #Loop para criar individuos dependendo da quantidade passada.
        caminhoRandom = random.sample(range(qtdPontos),qtdPontos)   #Criando lista de numeros aleatorios (caminho).
        distanciaCaminho = pontos.calcDistDeCaminhos(caminhoRandom) #Calculando distancia.
        indiv = I.Individuo(caminhoRandom, distanciaCaminho)        #Instanciando classe Individuo passando caminho e distancia.
        individuos.append(indiv)   #Adicionando individuo instanciado na lista.
    return individuos
