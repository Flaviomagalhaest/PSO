from .Config import Config_API, Config_PSO

def inicializaConfig(): 
    return Config_API(
        {'key' : 'AIzaSyC5wyAhlPFnEheBiT8i-XjpAajZ7i93eVQ',
        'txtEnderecos' : 'C:\\wamp64\\www\\pso\\py\\enderecos.txt',
        'transporte' : 'driving',
        'limitDia' : 2500,
        'limitRequi' : 100 })