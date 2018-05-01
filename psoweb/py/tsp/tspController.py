from py.tsp import PontosClass as P
from py.tsp import IndividuoClass as I
import random, json, copy

def calcMatrixDist(pontosJson):
    pontosObj = P.Pontos(dictPontos = pontosJson)    #Instanciando classe de Pontos. Passando dicionario de coord.
    pontosObj.calcMatrixDist()      #Calculando para cada ponto em Pontos, sua matriz distância.
    return pontosObj

def geraPopInicial(qtdPopInicial, qtdPontos, pontosJson):
    individuos = []    #Lista de individuos.
    pontos = P.Pontos(jsonSessao = pontosJson)    #Instanciando classe pontos passando string json.
    for i in range(0,qtdPopInicial):    #Loop para criar individuos dependendo da quantidade passada.
        caminhoRandom = random.sample(range(qtdPontos),qtdPontos)   #Criando lista de numeros aleatorios (caminho).
        caminhoRandom.append(caminhoRandom[0])  #Adicionando primeiro termo no final. O caminho tem que ser ciclico.
        distanciaCaminho = pontos.calcDistDeCaminhos(caminhoRandom) #Calculando distancia.
        indiv = I.Individuo(caminhoRandom, distanciaCaminho)        #Instanciando classe Individuo passando caminho e distancia.
        individuos.append(indiv)   #Adicionando individuo instanciado na lista.
    individuos = atualizaGbest(individuos)
    return individuos

def geraIteracao(iteracaoAtual, nrIteracoes, individuosJson, pontosJson):
    individuos = []    #Lista de individuos.
    pontos = P.Pontos(jsonSessao = pontosJson)    #Instanciando classe pontos passando string json.
    for i in range(0,len(individuosJson)): #Itera lista de individuos em Json para instanciar no objeto individuos
        individuo = I.Individuo(json=json.loads(individuosJson[i]))
        individuos.append(individuo)    #Lista de individuos já instanciados
    
    #Começando iterações
    for j in range(0,nrIteracoes):
        gbest = [i for i in individuos if i.gbest == True]  #Buscando o gbest da lista de individuos

        #Iterar cada individuo para crossover
        for indiv in individuos:
            qtdPontos = len(indiv.atual)
            #Gerando constantes para calculo incluindo pBest
            kPbest = random.randint(0, qtdPontos - 1)
            mPbest = random.randint(kPbest + 1, qtdPontos)
            #Gerando constantes para calculo incluindo gBest
            kGbest = random.randint(0, qtdPontos - 1)
            mGbest = random.randint(kGbest + 1, qtdPontos)
            #Fazendo crossover do caminho atual com o pbest
            indiv.atual = crossOver(indiv.atual, indiv.pbest, kPbest, mPbest)
            #Fazendo crossover do caminho atual com o gbest
            indiv.atual = crossOver(indiv.atual, gbest[0].atual, kGbest, mGbest)
            #Calculando nova distancia do individuo
            indiv.distAtual = pontos.calcDistDeCaminhos(indiv.atual)

        gbest = atualizaGbest(individuos)       #atualizando gbest
        individuos = atualizaPbest(individuos)  #atualizando pbest
    
    return individuos

def atualizaGbest(individuos):
    distGbest = 9999999999
    gbest = ''
    indice = 0
    for indiv in individuos:
        if indiv.distAtual < distGbest: #Verificando se o individuo tem uma distancia menor que o gbest
            distGbest = copy.copy(indiv.distAtual)  #Atualizando melhor distancia achada
            gbest = indice  #guardando indice do melhor individuo ate agora
        indiv.gbest = False #Resetando flag de gbest para o individuo
        indice += 1
    individuos[gbest].gbest = True  #Setando flag de gbest no individuo onde o índice foi salvo
    return individuos   #retornando lista de individuos com a flag de gbest setada para o melhor deles.

def atualizaPbest(individuos):
    for indiv in individuos:
        if indiv.distAtual < indiv.distPbest:
            indiv.distPbest = copy.copy(indiv.distAtual)
            indiv.pbest = copy.copy(indiv.atual)
    return individuos

def crossOver(caminhoDestino, caminhoBest, k, m):
    P = caminhoBest[k:m]    #Parte do caminho pBest ou gBest que irá ser introduzido no caminho original
    caminhoDestino = caminhoDestino[0 : (len(caminhoDestino) - 1)] #Retirando último ponto da lista.
    caminhoRetorno = P + caminhoDestino
    seen = set()
    caminhoRetorno = [x for x in caminhoRetorno if not (x in seen or seen.add(x))]  #Limpando a lista deixando apenas pontos distintos
    caminhoRetorno.append(caminhoRetorno[0])
    return caminhoRetorno