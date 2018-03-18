import IndivClass

indivs = []
gbest = ''

config {
    'nrIteracoes' : 100,
}

def inicializa(pontos,objetivo):
    #Transformando os pontos recebidos em individuos. Guardando numa lista
    #Calculando valor de fitness em seu construtor
    for ponto in pontos:
        indiv.append(IndivClass(ponto, objetivo))


def execute(objetivo):
    #Calculo de fitness e atualizacao do pbest
    for indiv in indivs:
        indiv.calculaFitness(objetivo)
        indiv.checaPbest()
    
    #Calcula gbest

def defineGbest():
    

    