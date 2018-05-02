from .PontoClass import Ponto
import math, json, copy

class Pontos(object):
    pontos = []                                     #Lista de objetos 'Ponto'.

    #Construtor recebe lista de coordenadas x e y. Cria lista de objetos 'Ponto'.
    def __init__(self, dictPontos=None, jsonSessao=None):
        #Construtor a partir de dicionario de coordenadas de pontos
        if (dictPontos != None):
            self.pontos = []
            for p in dictPontos:        #Foreach para cada coordenada da lista
                ponto = Ponto(p)        #Instanciando classe Ponto através da coordenada x e y obtida
                self.pontos.append(ponto)       #Adicionado objeto Ponto na lista

        #Construtor a partir de pontos em formato JSON salvos em sessão
        if(jsonSessao != None):
            listaPontos = json.loads(jsonSessao)    #Transformando json e um dicionario
            for p in listaPontos:
                ponto = Ponto(p)                #Instanciando Ponto
                ponto.matrixDist = p['matrix']  #Guardando matriz distancia
                self.pontos.append(ponto)            #Adicionando na lista

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
    
    #Recebe uma lista de Pontos (caminho) e retorna a distância entre eles
    def calcDistDeCaminhos(self, caminho):
        dist = 0
        for i in range(0, len(caminho)):    #Loop para checar toda a lista de inteiros (sequencia de pontos)
            if (i == len(caminho) - 1):     #Caso esteja no último termo
                dist += self.pontos[caminho[i]].matrixDist[caminho[0]]  #Soma a distância do último ponto ao primeiro.
                return dist
            dist += self.pontos[caminho[i]].matrixDist[caminho[i + 1]]  #Soma a distância total, a distância do ponto ao próximo
        return 'Erro em calcular distancia total do caminho'

    #Calcula para cada ponto da lista pontos seu fator heurístico.
    def calcFatorHeuristico(self):
        for i in range(0, len(self.pontos)):
            listaHeuristica = [i]
            while(listaHeuristica != []):
                listaHeuristica = self.definirListaHeuristica(i,listaHeuristica[-1], listaHeuristica)
            self.pontos[i].fatorHeuristico = self.pontos[i].fatorHeuristico[1:]

    def definirListaHeuristica(self, indiceOriginal, indiceLista, listaHeuristica):
        matrixDist = copy.copy(self.pontos[indiceLista].matrixDist)   #Copiando matriz distancia
        matrixDist[indiceLista] = max(matrixDist) #Serve apenas para que na linha abaixo ele não se ache.
        menorDist = min(matrixDist)     #Buscando a menor distância de sua matriz (ignorando ele próprio garças a linha acima)            
        indiceDoMenor = [i for i, j in enumerate(matrixDist) if j == menorDist] #Busca o índice da menor distância
        if indiceDoMenor[0] in listaHeuristica:
            self.pontos[indiceOriginal].fatorHeuristico = listaHeuristica
            return []   #Caso o indice achado já esteja na lista heurística
        else:
            listaHeuristica.append(indiceDoMenor[0])   #Adiciona maus um indice na lista
            return listaHeuristica

    def toJson(self):
        jsonRetorno = []
        for p1 in range(0,len(self.pontos)):
            pontoRetorno = ''
            pontoRetorno = {
                'x':self.pontos[p1].x,
                'y':self.pontos[p1].y,
                'matrix':self.pontos[p1].matrixDist
                'fatorHeuristico':self.pontos[p1].fatorHeuristico
            }
            jsonRetorno.append(pontoRetorno)
        return json.dumps(jsonRetorno)