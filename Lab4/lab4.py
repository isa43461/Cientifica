import math
import numpy as np

def f0(x,i):
	#derivadas de las funciones de f(x,i)
	if(i == 0):
		fx = 8*pow(x,3) + 3*pow(x,2) - 2*x
	elif(i == 1):
		fx = (-6)/pow(x,3)
	else:
		fx = (x-1)/(math.sqrt(pow(x,2) - 2*x + 3))
	return fx	

def f(x, i):
	#funciones a evaluar
	if(i == 0):
		fx = 2*pow(x,4) + pow(x,3) - pow(x,2) + 4
	elif(i == 1):
		fx = 3/pow(x,2)
	else:
		fx = math.sqrt(pow(x,2) - 2*x + 3) 
	return fx

''' Derivadas '''

def finitaAdelante(x,h):
	''' se aplica la ecuación f'(x) ≈ f(x + h) − f(x)
	                                  ---------------
	                                         h   
	Entrada: le ingresa un valor x y un desplazamiento h.
	Salida: Devuelve una lista con 3 valores por cada x, debido a que se 
	evalua en el ciclo las diferentes derivadas con ese x, 
	y se guardan en la lista.
	Funcionamiento: Se aplica la función de diferencia finita hacia adelante y se
	obtiene los resultados para cada función.
	'''
	l = []
	for i in range(3):
		l.append((f(x+h, i) - f(x, i))/h)
	return l

def finitaAtras(x,h):
	''' se aplica la ecuación f'(x) ≈ f(x) − f(x-h)
	                                  -------------
	                                         h     
	Entrada: le ingresa un valor x y un desplazamiento h.
	Salida: Devuelve una lista con 3 valores por cada x, debido a que se 
	evalua en el ciclo las diferentes derivadas con ese x, 
	y se guardan en la lista.  
	Funcionamiento: Se aplica la función de diferencia finita hacia atrás y se
	obtiene los resultados para cada función.
	'''
	l = []
	for i in range(3):
		l.append((f(x,i) - f(x-h, i))/h)
	return l

def finitaCentrada(x,h):
	''' se aplica la ecuación f'(x) ≈ f(x+h) − f(x-h)
	                                  -------------
	                                        2h       
	Entrada: le ingresa un valor x y un desplazamiento h.
	Salida: Devuelve una lista con 3 valores por cada x, debido a que se 
	evalua en el ciclo las diferentes derivadas con ese x, 
	y se guardan en la lista.
	Funcionamiento: Se aplica la función de diferencia finita centrada y se
	obtiene los resultados para cada función.
	'''
	l = []
	for i in range(3): #Se hace un ciclo por las 3 derivadas existentes.
		l.append((f(x+h, i) - f(x-h, i))/(2*h))
	return l

''' Integrales '''

def fi(x, i):
	#funciones de las integrales a evaluar
	if(i == 0):
		fx = x*math.sin(x)
	elif(i == 1):
		fx = math.exp(x)*math.cos(x)
	else:
		fx = x*math.sqrt(1 + x) 
	return fx
	
def rectangulo(n,x):
	'''
	Entrada: Recibe la longitud de la lista n y la lista x.
	Salida: Retorna una lista con la regla del punto medio para cada
	integral definida.
	Funcionamiento: Se aplica la función dada en clase.
	'''
	l = []
	for k in range(3):
		ans = 0
		for i in range(1,n):	
			ans += (x[i] - x[i-1])*fi(((x[i-1] + x[i])/2), k)
		l.append(ans)
	return l

def trapezoide(n,x):
	'''
	Entrada: Recibe la longitud de la lista n y la lista x.
	Salida: Retorna una lista con la regla del trapezoide para cada
	integral definida.
	Funcionamiento: Se aplica la función dada en clase.
	'''
	l = []
	for k in range(3):
		ans = 0
		for i in range(1,n):	
			ans += (x[i] - x[i-1])*(fi(x[i-1], k) + fi(x[i], k))
		l.append(ans/2)
	return l

def simpons(n,x):
	'''
	Entrada: Recibe la longitud de la lista n y la lista x.
	Salida: Retorna una lista con la regla de Simpson para cada
	integral definida.
	Funcionamiento: Se aplica la función dada en clase.
	'''
	l = []
	for k in range(3):
		ans = 0
		for i in range(1,n):	
			ans += (x[i] - x[i-1])*(fi(x[i-1],k) + 4*fi(((x[i-1] + x[i])/2), k) + fi(x[i], k))
		l.append(ans/6)
	return l
