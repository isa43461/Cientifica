from lab4 import simpons,trapezoide, rectangulo, finitaCentrada, finitaAtras, finitaAdelante, f0
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
from time import time

def main():
	n0 = 1000
	x = np.linspace(2,10,n0)
	l1 = [0 for _ in range(n0)]
	l2 = [0 for _ in range(n0)]
	l3 = [0 for _ in range(n0)]
	deriv1 = [0 for _ in range(n0)]
	deriv2 = [0 for _ in range(n0)]
	deriv3 = [0 for _ in range(n0)]
	h = 1; 
	#h = 1.5
	#h = 0.5 
	#h = 0.1
	n = 1000; a = 0; b = 1
	l = np.linspace(a,b,n)
	l = [round(l[i],1) for i in range(n)]
	time1 = [0 for _ in range(n0)]; time2 = [0 for _ in range(n0)]; time3 = [0 for _ in range(n0)]
	for i in range(n0):
		#Se llama a la función finitaAdelante
		inicio = time()
		l1[i] = finitaAdelante(x[i],h)
		elapsed_time = time() - inicio
		time1[i] = elapsed_time
		#Se llama a la función finitaAtras
		inicio = time()
		l2[i] = finitaAtras(x[i],h)
		elapsed_time = time() - inicio
		time2[i] = elapsed_time
		#Se llama a la función finitaCentrada
		inicio = time()
		l3[i] = finitaCentrada(x[i],h)
		elapsed_time = time() - inicio
		time3[i] = elapsed_time

	print("Tiempo finitaAdelante",stats.mean(time1))
	print("Tiempo finitaAtras",stats.mean(time2))
	print("Tiempo finitaCentrada",stats.mean(time3))


	print("Rectangulo: ",rectangulo(n,l))
	print("Trapezoide: ",trapezoide(n,l))
	print("Simpons: ",simpons(n,l))

	#se sacan los valores pertinentes de cada función (adelante, atras, centrada)
	l1f1 = []; l2f1 = []; l3f1 = []
	l1f2 = []; l2f2 = []; l3f2 = []
	l1f3 = []; l2f3 = []; l3f3 = []
	for i in range(n0):
		deriv1[i] = f0(x[i],0)
		deriv2[i] = f0(x[i],1)
		deriv3[i] = f0(x[i],2)
		l1f1.append(l1[i][0])#adelante funcion 1
		l1f2.append(l1[i][1])#adelante funcion 2
		l1f3.append(l1[i][2])#adelante funcion 3
		l2f1.append(l2[i][0])#atras funcion 1
		l2f2.append(l2[i][1])#atras funcion 2
		l2f3.append(l2[i][2])#atras funcion 3
		l3f1.append(l3[i][0])#centrada funcion 1
		l3f2.append(l3[i][1])#centrada funcion 2
		l3f3.append(l3[i][2])#centrada funcion 3

	''' errores  función 1'''
	errorAdelante1 = abs((np.array(l1f1)-np.array(deriv1))/deriv1)
	error_tipicoAd1 = np.std(errorAdelante1)
	errorMAdelante1 = stats.mean(errorAdelante1)
	print("Error medio adelante funcion1: ",errorMAdelante1)
	print("Desviación estandar adelante funcion1: ",error_tipicoAd1)
	print()
	errorAtras1 = abs((np.array(l2f1)-np.array(deriv1))/deriv1)
	error_tipicoAt1 = np.std(errorAtras1)
	errorMAtras1 = stats.mean(errorAtras1)
	print("Error medio atrás funcion1: ",errorMAtras1)
	print("Desviación estandar atrás funcion1: ",error_tipicoAt1)
	print()
	errorCentrada1 = abs((np.array(l3f1)-np.array(deriv1))/deriv1)
	error_tipicoC1 = np.std(errorCentrada1)
	errorMCentrada1 = stats.mean(errorCentrada1)
	print("Error medio centrada funcion1: ",errorMCentrada1)
	print("Desviación estandar centrada funcion1: ",error_tipicoC1)


	'''___________________________________________________________'''
	errorAdelante2 = abs((np.array(l1f2)-np.array(deriv2))/deriv2)
	error_tipicoAd2 = np.std(errorAdelante2)
	errorMAdelante2 = stats.mean(errorAdelante2)
	print("Error medio adelante funcion2: ",errorMAdelante2)
	print("Desviación estandar adelante funcion2: ",error_tipicoAd2)
	print()
	errorAtras2 = abs((np.array(l2f2)-np.array(deriv2))/deriv2)
	error_tipicoAt2 = np.std(errorAtras2)
	errorMAtras2 = stats.mean(errorAtras2)
	print("Error medio atrás funcion2: ",errorMAtras2)
	print("Desviación estandar atrás funcion2: ",error_tipicoAt2)


	errorCentrada2 = abs((np.array(l3f2)-np.array(deriv2))/deriv2)
	errorMCentrada2 = stats.mean(errorCentrada2)
	error_tipicoC2 = np.std(errorCentrada2)
	print("Error medio centrada funcion2: ",errorMCentrada2)
	print("Desviación estandar centrada funcion2: ",error_tipicoC2)

	'''___________________________________________________________'''
	print()
	errorAdelante3 = abs((np.array(l1f3)-np.array(deriv3))/deriv3)
	error_tipicoAd3 = np.std(errorAdelante3)
	errorMAdelante3 = stats.mean(errorAdelante3)
	print("Error medio adelante funcion3: ",errorMAdelante3)
	print("Desviación estandar adelante funcion3: ",error_tipicoAd3)
	print()
	errorAtras3 = abs((np.array(l2f3)-np.array(deriv3))/deriv3)
	error_tipicoAt3 = np.std(errorAtras3)
	errorMAtras3 = stats.mean(errorAtras3)
	print("Error medio atrás funcion3: ",errorMAtras3)
	print("Desviación estandar atrás funcion3: ",error_tipicoAt3)
	print()
	errorCentrada3 = abs((np.array(l3f3)-np.array(deriv3))/deriv3)
	error_tipicoC3 = np.std(errorCentrada3)
	errorMCentrada3 = stats.mean(errorCentrada3)
	print("Error medio centrada funcion3: ",errorMCentrada3)
	print("Desviación estandar centrada funcion3: ",error_tipicoC3)

	'''graficas'''

	#función número 1
	'''
	plt.plot(x,l1f1,'-', label = "finitaAdelante funcion 1")
	plt.plot(x,l2f1,'-', label = "finitaAtras funcion 1")
	plt.plot(x,l3f1,'-', label = "finitaCentrada funcion 1")
	plt.plot(x,deriv1,'-', label = "Analitica funcion 1")


	#función número 2
	
	plt.plot(x,l1f2,'-', label = "finitaAdelante funcion 2")
	plt.plot(x,l2f2,'-', label = "finitaAtras funcion 2")
	plt.plot(x,l3f2,'-', label = "finitaCentrada funcion 2")
	plt.plot(x,deriv2,'-', label = "Analitica funcion 2")

	#función número 3 

	plt.plot(x,l1f3,'-', label = "finitaAdelante funcion 3")
	plt.plot(x,l2f3,'-', label = "finitaAtras funcion 3")
	plt.plot(x,l3f3,'-', label = "finitaCentrada funcion 3")
	plt.plot(x,deriv3,'-', label = "Analitica funcion 3")
	
	plt.legend()
	plt.grid()
	plt.title("Gráficas")
	plt.savefig("0.5_fun2.png")
	plt.show()'''
main()