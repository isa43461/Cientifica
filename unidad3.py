import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
def superior(a,b): #función de sistemas triangulares superiores
	"""
	Entrada: el parametro "a" hace referencia a una matriz nxn que tiene la forma de matriz superior, la cual es la que se pretende resolver
			con el metodo de sustitucion sucesiva hacia atras, b es un arreglo [0...n].
	Salida: un arreglo solve[0...n] donde for solve[i] = xi donde 0 <= i < n
	Funcionamiento: en esta implementacion se pretende realizar una sucesion sucesiva hacia atrás
					donde en primer lugar se como la formula a remplazar por cada xi simepre se tiene
					bi - sumatoria, se añade a solve cada valor de bi, posteriormente se haya el valor xn
					y con base en eso se realiza la sumatoria en donde en cada solve[i] se va acumulando el valor
					que le coresponde, esto se realiza desde i = n-2 (por notacion de python) hasta 0.
	"""
	n = len(b)
	solve =[b[i] for i in range(n)]
	solve[n-1] = b[n-1]/a[n-1][n-1]
	i = n-2
	while i >= 0:
		for j in range(i+1,n):
			solve[i] = solve[i] - (a[i][j]*solve[j])
		solve[i] = solve[i]/a[i][i]
		i -=1
	return solve

def inferior(a,b): #función de sistemas triangulares inferiores
	n = len(b)
	solve =[b[i] for i in range(n)]
	solve[0] = b[0]/a[0][0]
	for i in range(1,n):
		for j in range(i):
			solve[i] = solve[i] - (a[i][j]*solve[j])
		solve[i] = solve[i]/a[i][i]
	return solve

def ecuacionesN(Ax,b,o):
	"""
	Entrada: Recibe un arreglo Ax[0...n] y un arreglo b[0...n] donde n es la longitud de los arreglos
	Salida: Retorna los minimos cuadrados aplicando el metodo de ecuaciones normales.
	Funcionamiento: Se crea una matriz A de tal forma que se pueda aplicar pow(t,i) dependiendo del
	numero de columnas(parametros) que pase la funcion. Despues se hace la traspuesta de esa matriz A
	para poder multiplicarlas. Con esa misma matriz transpuesta AT, se multiplica b de manera que 
	obtengamos una columna resultante y finalmente, se aplica la funcion cholesky, se hace la transpuesta
	del resultado de la matriz en la que se aplico cholesky y finalmente se llaman las funciones de
	sistemas triangulares inferiores y superiores.
	"""

	n = len(Ax)
	A = [[0 for i in range(o)] for j in range(n)]
	for i in range(n):
		for j in range(o):
			A[i][j] = pow(Ax[i],j)

	AT = np.transpose(A)
	A = np.dot(AT, A)
	b = np.dot(AT, b)
	L = np.linalg.cholesky(A)
	LT = np.transpose(L)
	y = inferior(L, b)
	x = superior(LT, y)
	return x

def HouseHolder(Ax,b,o):
	"""
	Entrada: Recibe un arreglo Ax[0...n] y un arreglo b[0...n] donde n es la longitud de los arreglos
	Salida: Retorna los minimos cuadrados aplicando el metodo de ecuaciones normales.
	Funcionamiento: Se crea una matriz A de tal forma que se pueda aplicar pow(t,i) dependiendo del
	numero de parametros(cols) que pase la funcion. Se recorre respecto al numero de parametros(cols)
	y se crea un arreglo aux y un arreglo col que sirve para escoger los datos x su columna respectiva y se
	garantiza poner los 0 en las posiciones que debe ir dependiendo del puntero. Se le aplica al arreglo col
	la norma para poder hacer la resta entre columnas, se garantiza el signo del alpha (contrario al del puntero).
	Se aplica la formula H, se multiplica H por el arreglo A y por la col B. Finalmente se actualiza los nuevos
	valores de A y B. Retorna el resultado de la funcion superior a la cual se le pasa el arreglo desde 
	A[0..o][0..o] y b[0..o] donde o es el numero de parametros.
	"""
	n = len(Ax)
	A = [[0 for i in range(o)] for j in range(n)]
	for i in range(n):
		for j in range(o):
			A[i][j] = pow(Ax[i],j)

	for i in range(o):
		aux = [0 for _ in range(n)]
		col = [A[j][i] for j in range(n)]
		for s in range(i):
			col[s] = 0
		norma = np.linalg.norm(col)
		if(col[i] >= 0):
			aux[i] = (-1)*norma
		else:
			aux[i] = norma
		v = np.array(col) - np.array(aux)
		a = np.array(v)[np.newaxis] #Se utiliza newaxis para poder hacer la transpuesta correcta del vector v
		vt = np.transpose(a)
		vvt = np.array(np.multiply(v,vt))
		vtv = 0
		for i in range(n):
			vtv += vt[i]*v[i]
		H = np.identity(n)-np.multiply(np.divide(vvt,vtv),2)
		HA = np.dot(H,A)
		HB = np.dot(H,b)
		A = HA
		b = HB
	R = A[0:o,0:o]
	y = b[0:o]
	ans = superior(R,y)
	return ans
