class Ponto(object):
    x = 0
    y = 0
    matrixDist = []     #Matriz de distâncias para demais pontos
    fatorHeuristico = []    #Lista de pontos vizinhos mais próximos até não houver repetição.
    
    def __init__(self, end):
        self.matrixDist = []
        self.x = end['x']
        self.y = end['y']