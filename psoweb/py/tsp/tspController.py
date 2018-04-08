from py.tsp import PontosClass as P

def calcMatrixDist(pontosJson):
    pontosObj = P.Pontos(pontosJson)    #Instanciando classe de Pontos. Passando lista json
    pontosObj.calcMatrixDist()      #Calculando para cada ponto em Pontos, sua matriz distância.
    return pontosObj

def geraPopInicial(qtdPopInicial, qtdPontos):
    pass
