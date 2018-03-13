"""PSO"""
# -*- coding: utf-8 -*-
import copy
import lib
from IndivClass import Individuo, Caminho


class PSO(object):    
    config = ''
    pontos = ''
    individuos = []
    gbest = ''
    log1 = []
    log2 = []        
    def __init__(self, config, nrCidades, pontos):
        #  Gravando configurações na instância
        self.config = config
        # Gravando pontos de destino
        self.pontos = pontos        
        # Inicializando Gbest
        self.gbest = Caminho()
        # Loop que cria os indivíduos e adiciona na lista
        for i in range(0, config.nr_indiv):            
            indiv = Individuo(nrCidades)
            indiv.atual.calcDistancia(pontos)
            self.individuos.append(indiv)
        self.gera_pbest()
        self.gera_gbest()
    
    def gera_pbest(self):
        for indiv in self.individuos:        
            if (indiv.pbest.distTotal == 0) or (indiv.pbest.distTotal > indiv.atual.distTotal):
                indiv.pbest = copy.deepcopy(indiv.atual)
    
    def gera_gbest(self):        
        if (self.gbest.distTotal == 0):
            self.gbest = copy.deepcopy(self.individuos[0].atual)
        for indiv in self.individuos:
            if (self.gbest.distTotal > indiv.atual.distTotal) : 
                self.gbest = copy.deepcopy(indiv.atual)              
    
    def crossover(self, original, adicional, k, m):
        lista = copy.deepcopy(original)
        adc = copy.deepcopy(adicional)
        del lista[-1]
        del adc[-1]
        result = []
        result = list((adc[k : k + m]) + [x for x in lista if x not in adc[k:k+m]])               
        result.append(result[0])
        return result
        
                
                
    def gera_iteracoes(self, nrTotal):
        for i in range(0, nrTotal):
            
            for indiv in self.individuos:
                indiv.gera_constant()                        
                
                result = list(self.crossover(indiv.atual.caminho,
                                        indiv.pbest.caminho, 
                                        indiv.k[0], indiv.m[0]))                
                indiv.atual.caminho = list(self.crossover(result,
                                            self.gbest.caminho, 
                                            indiv.k[1], indiv.m[1]))
                indiv.atual.calcDistancia(self.pontos)

            self.gera_pbest()
            self.gera_gbest()    
        return self         
                         
            
                
                
        