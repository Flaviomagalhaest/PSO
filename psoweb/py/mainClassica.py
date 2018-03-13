"""mainClassica"""
# -*- coding: utf-8 -*-
import sys

# ex = sys.argv[1]    #NOME DO PROBLEMA A SER RESOLVIDO
# exemplo = 'C:\\wamp64\\www\\pso\\files\\rotas\\'+ex+'.txt'    
exemplo = 'C:\\wamp64\\www\\pso\\files\\rotas\\XQF131.txt'    
with open(exemplo,'r') as f:
    for line in f:
        print(line)
