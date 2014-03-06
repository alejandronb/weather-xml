#coding: utf-8
import requests
import json
from jinja2 import Template
import webbrowser
import os
import requests
from lxml import etree


ciudades = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Sevilla']
f = open("plantilla.html","r")
salida = open("salida.html","w")
html = ''


for linea in f:
	html += linea


temp_max = []
temp_min = []
viento_km = []
direccion_viento = []


url = 'http://api.openweathermap.org/data/2.5/weather'

for ciudad in ciudades:
	parametros = {'q':'%s,spain' % ciudad,'mode':'xml','units':'metric','lang':'es'}
	peticion = requests.get(url,params=parametros)
	raiz = etree.fromstring(peticion.text.encode("utf-8"))
	city = raiz.find("city")
	ncity = city.attrib["name"]
	temperature = raiz.find("temperature")
	tempmax = round(float(temperature.attrib["max"]),1)
	tempmin = round(float(temperature.attrib["min"]),1)
	viento_dir = raiz.find("wind/direction")
	direccion = viento_dir.attrib["name"]
	viento_vel = raiz.find("wind/speed")
	velocidad = viento_vel.attrib["value"]
	temp_max.append(tempmax)
	temp_min.append(tempmin)
	viento_km.append(velocidad)
	direccion_viento.append(direccion)



template = Template(html)
template = template.render(ciudades=ciudades,maxima=temp_max,minima=temp_min,viento=viento_km,direccion=direccion_viento)
salida.write(template)
webbrowser.open("salida.html")


