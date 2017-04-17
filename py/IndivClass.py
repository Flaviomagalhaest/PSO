# -*- coding: utf-8 -*-
from random import shuffle, randint

class Individuo(object):
    atual = ''
    pbest = ''
    m = []
    k = []
    
    # Instância atual, pbest e gbest na classe caminho e sorteia população inicial
    def __init__(self, totalDeCidades):
        self.atual = Caminho()
        self.pbest = Caminho()
                
        self.atual.caminho = self.geraPopInicial(totalDeCidades)
    
    # Gera lista com população inicial
    def geraPopInicial(self, total):        
        lista = []
        for i in range(0, total):
            lista.append(i)
        shuffle(lista)
        lista.append(lista[0])
        return lista

    def gera_constant(self):
        self.k = []
        self.m = []
        for i in range (0, 2):
            self.k.append(randint(0, len(self.atual.caminho) - 1))
            self.m.append(randint(1, len(self.atual.caminho) - self.k[i]))
                    
    
class Caminho(object):
    caminho = []        
    distTotal = 0
    
    def __init__(self):
        pass
    
    def calcDistancia(self, pontos):
        self.distTotal = 0
        for i in range(0, len(self.caminho)):
            if (i == len(self.caminho) - 1):
                j = 0
            else:
                j = i+1
            self.distTotal += pontos.lista[self.caminho[i]].matrixDist[self.caminho[j]]['distance']['value']
                                
        
        

