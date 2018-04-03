from .PontoClass import Ponto
import math
import json

class Pontos(object):
    pontos = []                                     #Lista de objetos 'Ponto'.

    #Construtor recebe lista de coordenadas x e y. Cria lista de objetos 'Ponto'.
    def __init__(self, dictPontos):
        self.pontos = []
        for p in dictPontos:        #Foreach para cada coordenada da lista
            ponto = Ponto(p)        #Instanciando classe Ponto através da coordenada x e y obtida
            self.pontos.append(ponto)       #Adicionado objeto Ponto na lista

    def calcMatrixDist(self):
        for p1 in range(0,len(self.pontos)):        #loop primário
            for p2 in range(0,len(self.pontos)):    #loop secundário da mesma lista de pontos
                x1 = self.pontos[p1].x
                y1 = self.pontos[p1].y
                x2 = self.pontos[p2].x
                y2 = self.pontos[p2].y
                distancia = math.hypot(x2 - x1, y2 - y1)    #cálculo de distância (Reta)
                self.pontos[p1].matrixDist.append(distancia)    #Salvando distância na lista de matriz distância
                                                                #Do objeto ponto em questão
    def toJson(self):
        jsonRetorno = []
        for p1 in range(0,len(self.pontos)):
            pontoRetorno = ''
            pontoRetorno = {
                'x':self.pontos[p1].x,
                'y':self.pontos[p1].y,
                'matrix':self.pontos[p1].matrixDist
            }
            jsonRetorno.append(pontoRetorno)
        return json.dumps(jsonRetorno)