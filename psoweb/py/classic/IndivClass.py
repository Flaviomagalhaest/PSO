# -*- coding: utf-8 -*-
import math
from random import random
class Individuo(object):
    atual = {}
    pbest = {}
    fitnessAtual = ''
    fitnessPbest = 9999999999
    velocidade = {}

    #Calcula valor de fitness com base em sua posicao atual
    def calculaFitness(self, objetivo):
        x1 = self.atual['x']
        y1 = self.atual['y']
        x2 = objetivo['x']
        y2 = objetivo['y']
        self.fitnessAtual = math.hypot(x2 - x1, y2 - y1)

    #Checa se a posicao atual é melhor que o pbest
    def checaPbest():
        if (self.fitnessAtual <= self.fitnessPbest):
            self.fitnessPbest = self.fitnessAtual
            self.atual = dict(self.pbest)
    
    #Calcula a nova velocidade
    def calcVelocidade(self,dimension,const, gbest):
        novaVel = (float(const['c1']) * random() * (self.pbest[dimension] - self.atual[dimension]) +
        float(const['c2']) * random() * (gbest.atual[dimension] - self.atual[dimension]))
        self.velocidade[dimension] += novaVel

    def __init__(self, ponto, objetivo):
        self.atual = dict(ponto)
        self.pbest = dict(self.atual)
        self.velocidade = {'x':0, 'y':0}
        #Calculando valor de fitness através do objetivo
        self.calculaFitness(objetivo)
        self.fitnessPbest = self.fitnessAtual