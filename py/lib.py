# -*- coding: utf-8 -*-

# Retorna uma lista dos itens presentes no arquivo txt
def lerEnderecoTXT(lista, arquivo):
    with open(arquivo) as f:
        for item in f:
            lista.append(item)
    return lista
    
# Algoritmo para tratar limite de requisições do GoogleMaps
# Calcula os valores máximos que a API suporta em uma requisição
# x numero de items a calcular matriz. y número total
# retorna lista com os números de 'x' segmentados para uso da API
def verificaLimite(limitDia, limitRequi, y):
    total = y * y
    cont = 0
    items = []
    items.append(0)
    if (total > limitDia):
        print('O valor de items da matriz distância é superior ao limite diário suportado pela API')
    else:
        if (y > limitRequi):
            print('O valor de itens da coluna da matriz é superior ao número suporado por requisição da API')
        else:
            x = limitRequi/y
            x = int(x)
            while (cont + x <= y):
                cont += x
                items.append(cont)
            if not (cont == y):
                items.append(y)
    return items
        
def gravarLog(arquivo, lista, adicional, k, m, result):
    with open(arquivo, 'w') as f:
        f.write('lista: '+str(lista)+'\n')
        f.write('adicional: '+str(adicional)+'\n')
        f.write('k: '+str(k)+'\n')
        f.write('m: '+str(m)+'\n')
        f.write('result: '+str(result)+'\n')
        f.write('\n')

def SerializarObjJSON(objeto_pso):
    import json
    MeuJson = {}
    gbest = {}
    pontos = {}
    #gbest
    gbest['caminho'] = objeto_pso.gbest.caminho
    gbest['distTotal'] = objeto_pso.gbest.distTotal
    MeuJson['gbest'] = gbest
    #pontos
    i = 0
    for item in objeto_pso.pontos.coords:
        pontos[i] = item
        i = i + 1
    MeuJson['pontos'] = pontos
    return json.dumps(MeuJson)
    
    
        
