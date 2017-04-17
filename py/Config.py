# -*- coding: utf-8 -*-
class Config_API(object):
    
    key = ''
    txtEnderecos = ''
    transporte = ''
    limitDia = 0
    limitRequi  = 0
    
    
    def __init__(self, configs):
        self.key = configs['key']
        self.txtEnderecos = configs['txtEnderecos']
        self.transporte = configs['transporte']
        self.limitDia = configs['limitDia']
        self.limitRequi = configs['limitRequi']


class Config_PSO(object):
    nr_indiv = 0
    
    def __init__(self, configs):
        self.nr_indiv = configs['nr_indiv']
        
