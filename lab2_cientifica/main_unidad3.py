from unidad3 import ecuacionesN, HouseHolder
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
from time import time

def main():
	#datos de la temperatura

	y = [31.0, 23.2, 22.4, 21.6, 20.8, 19.8, 19.8, 19.4, 19.1, 18.5, 18.1, 17.8, 17.6, 17.3, 17.2, 17.2, 18.4, 19.5, 21.7, 24.7, 26.5, 27.6, 28.0, 27.6, 26.3, 24.9, 22.9, 20.9, 19.9, 19.6, 19.0, 18.6, 18.3, 18.0, 17.7, 17.4, 17.1, 16.9, 16.7, 16.4, 17.6, 19.6, 21.6, 23.8, 25.9, 26.5, 26.8, 26.4, 25.6, 24.1, 21.9, 20.0, 19.0, 18.7, 18.5, 18.4, 18.1, 18.0, 17.6, 17.4, 17.6, 17.6, 17.4, 17.0, 18.0, 19.6, 21.2, 23.5, 25.5, 26.9, 26.6, 25.5, 23.7, 22.0, 20.8, 19.4, 18.7, 18.6, 18.1, 18.0, 18.1, 18.3, 17.9, 17.6]
	nn = len(y)
	t = np.arange(0, 8.4, 0.1) #arreglo t para datos de la temperatura(creacion de arreglo de la longitud de y tal que vaya de 0.1 en 0.1)

	#datos de punto de rocio
	#y = [16.2, 18.1, 18.9, 18.5, 17.7, 17.7, 17.5, 17.3, 16.9, 16.7, 16.5, 16.3, 16.2, 15.9, 16.0, 16.7, 16.8, 17.6, 19.3, 18.2, 17.8, 17.8, 17.3, 16.0, 18.1, 18.1, 17.6, 17.0, 17.1, 16.8, 16.3, 16.2, 16.2, 16.0, 16.0, 15.7, 15.6, 15.3, 15.2, 15.8, 16.8, 17.4, 17.6, 17.6, 17.1, 18.0, 17.7, 17.4, 18.3, 18.3, 17.9, 17.3, 17.1, 16.9, 16.9, 16.3, 16.3, 16.1, 16.1, 16.8, 16.8, 16.5, 16.3, 16.9, 17.5, 17.9, 18.0, 17.7, 17.4, 17.2, 17.8, 18.0, 18.3, 17.9, 17.1, 16.7, 16.5, 16.1, 16.0, 16.4, 16.5, 16.3, 16.1]
	#nn = len(y)
	#t = np.arange(0, 8.3, 0.1) #arreglo t para datos del punto de rocio

	''' ___________________________________________________________________'''

	n = 4 #numero de cols que habran
	entT = []; entY = []; valT = []; valY = []

	#Separacion de datos de entrenamiento y validacion
	for i in range(nn):
		if(i%2 == 0):
			entT.append(t[i])
			entY.append(y[i])
		else:
			valT.append(t[i])
			valY.append(y[i])

	start_time = time()
	x = ecuacionesN(entT,entY,n)
	elapsed_time = time() - start_time
	print("Elapsed time of EcN: %.10f seconds." % elapsed_time) #tiempo de funcion de ecuaciones normales

	t_1 = np.linspace(min(t),max(t), num=1000)

	start_time1 = time()
	hh = HouseHolder(entT,entY,n)
	elapsed_time1 = time() - start_time1
	print("Elapsed time of HouseHolder: %.10f seconds." % elapsed_time1) #tiempo de ejecucion HouseHolder

	ym = 0 ; yn = 0 ; lg = len(hh)
	for i in range(lg):
		ym += (x[i]*pow(t_1,i)) #polinomio para ecuacionesN
		yn += (hh[i]*pow(t_1,i)) #polinomio para HouseHolder
	
	ym = [round(ym[i],1) for i in range(1000)] #redondeo
	yn = [round(yn[i],1) for i in range(1000)]

	#Error

	ymv = 0 ; ynv = 0
	for i in range(lg):
		ymv += (x[i]*pow(np.array(valT),i))
		ynv += (hh[i]*pow(np.array(valT),i))

	errorAbsEcN = abs((ymv - valY)) #error absoluto para ecuacionesN
	errorAbsHH = abs((ynv - valY)) #error absoluto para HouseHolder

	errorMedioEcN = stats.mean(errorAbsEcN) #error medio para ecuacionesN
	errorMedioAbsHH = stats.mean(errorAbsHH) #error medio para HouseHolder

	errorMedioAbsHH = round(errorMedioAbsHH,2) #redondeo del error medio
	errorMedioEcN = round(errorMedioEcN,2)

	error_tipicoEc = np.std(errorAbsEcN) #error tipico para ecuacionesN
	error_tipicoHH = np.std(errorAbsHH) #error tipico para HouseHolder

	print("El error medio con EcN es: ",errorMedioEcN)
	print("El error medio es HH: ",errorMedioAbsHH)
	print("El error típico es Ec: ",error_tipicoEc)
	print("El error típico es HH: ",error_tipicoHH)

	'''Gráficas de House Holder y ecuaciones normales'''

	plt.plot(entT,entY,'o', label = "puntos de Ent")
	plt.plot(valT,valY,'o', label = "puntos de Val")
	plt.plot(t_1, ym,label="EcuacionesN")
	plt.plot(t_1, yn, label="HouseHolder")
	plt.legend()
	plt.grid()
	plt.title("Gráficas")
	#plt.savefig('n12_2eN.png')
	plt.show()
main()
