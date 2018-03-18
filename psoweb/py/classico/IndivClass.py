# -*- coding: utf-8 -*-
import math
class Individuo(object):
    atual = {}
    pbest = {}
    fitnessAtual = ''
    fitnessPbest = 9999999999

    def __init__(self, ponto, objetivo):
        self.atual['x'] = ponto['x']
        self.atual['y'] = ponto['y']
        self.pbest = dict(self.atual)
        #Calculando valor de fitness através do objetivo
        self.fitnessAtual = calculaFitness(objetivo)
    
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