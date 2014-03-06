#coding: utf-8
import requests
import json
from jinja2 import Template
import webbrowser
import os
import requests
from lxml import etree


ciudades = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla']
f = open("plantilla.html","r")
salida = open("salida.html","w")
html = ''

def cardinalidad(direccion):
	"Funcion que transforma los grados en cardinalidades"
	for degree in str(direccion):
		if direccion >= 337.5 and direccion < 22.5:
			return "N"
		elif direccion >= 22.5 and direccion < 67.5:
			return "NE"
		elif direccion >= 67.5 and direccion < 112.5:
			return "E"
		elif direccion >= 112.5 and direccion < 157.5:
			return "SE"
		elif direccion >= 157.5 and direccion < 202.5:
			return "S"
		elif direccion >= 202.5 and direccion < 247.5:
			return "SO"
		elif direccion >= 247.5 and direccion < 292.5:
			return "O"
		elif direccion >= 292.5 and direccion < 337.5:
			return "NO"


for linea in f:
	html += linea


temp_max = []
temp_min = []
viento_km = []
direccion_viento = []

#r = request.get .........
#elemento_raiz = etree.fromstring(r.text.encode("utf-8"))


url = 'http://api.openweathermap.org/data/2.5/weather'



for ciudad in ciudades:
	parametros = {'q':'%s,spain' % ciudad,'mode':'xml','units':'metric','lang':'es'}
	peticion = requests.get(url,params=parametros)
	#elemento_raiz = etree.fromstring(peticion.text.encode("utf-8"))
	print peticion.text
#	viento = 
#	direccion = 
#	tempmax = 
#	tempmin = 
#	maxima = round(tempmax - 273,1)
#	minima = round(tempmin - 273,1)
#	vientokm = round(viento*1.61)
#	temp_max.append(maxima)
#	temp_min.append(minima)
#	viento_km.append(vientokm)
#	direccion_viento.append(cardinalidad(direccion))


#template = Template(html)
#template = template.render(ciudades=ciudades,maxima=temp_max,minima=temp_min,viento=viento_km,direccion=direccion_viento)
#salida.write(template)
#webbrowser.open("salida.html")


