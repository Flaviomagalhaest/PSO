python 3.6

#Atualizando pip
py -m pip install -U pip

#Instalando django
py -m pip install django

#Instalando virtualenv
py -m pip install virtualenvwrapper-win

#Criando diretório virtual para nosso projeto
py -m virtualenv djangodev

#Criando projeto django. Ele irá auto-gerar alguns códigos default do framework
py -m django startproject psoweb

#Para start o django e o ver rodando
py manage.py runserver

#Criando um app
py manage.py startapp --nomeApp--

#Instalando GoogleMaps package
py -m pip install -U googlemaps


