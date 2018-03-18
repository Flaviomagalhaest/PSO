import IndivClass

config {
    'nrIteracoes' : 100,
}

def inicializa(pontos,objetivo):
    indivs = []
    gbest = ''
    #Transformando os pontos recebidos em individuos. Guardando numa lista
    #Calculando valor de fitness em seu construtor
    for ponto in pontos:
        indiv.append(IndivClass(ponto, objetivo))

def execute(objetivo):

    