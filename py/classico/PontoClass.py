"""Classe de Pontos"""
# -*- coding: utf-8 -*-
import lib 

class Pontos(object):          
    lista = []
    coords = []        
    
    def __init__(self, listaEnderecos, gmaps):
        # Instanciando os pontos obtidos    
        for end in listaEnderecos:            
            p = Ponto(end)            
            self.lista.append(p)
            self.coords.append(p.coordenada)        
        
    def calcMatrixDist(self, transporte, limitDia, limitReq):
        flg_coord = 0
        matrix = []
        # Verifica se tamanho da matriz não ultrapassa limite da API
        y = len(self.coords)

        # Busca lista dos índices que separará requisições
        listSeg = lib.verificaLimite(limitDia, limitReq, y)
        for i in range(1, len(listSeg)):                        
            # Fazer requisição que retorna Matriz distancia 
            matrix = self.gmaps.distance_matrix(self.coords[listSeg[i-1]:listSeg[i]],
                                                     self.coords,
                                                     transporte,
                                                     'pt-BR')
            #print(matrix)                                                                
            # loop para registrar os dados da matriz entre os pontos individuais 
            z = 0
            for flg_coord in range(flg_coord, flg_coord + len(matrix['origin_addresses'])):
               #print(flg_coord, z)
               self.lista[flg_coord].matrixDist = matrix['rows'][z]['elements']
               z += 1
            flg_coord += 1                     
                               
                   

class Ponto(object):
    
    infos = ''
    endereco = ''
    coordenada = ''
    matrixDist = [] 
    
    def __init__(self, end):
        self.coordenada = end      
        

    
    
    
