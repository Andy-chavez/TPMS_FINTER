from scipy.interpolate import lagrange
import numpy as np
# se podra usar? de todas formas no ayuda mucho con el hecho de que hay que mostrar los pasos,
# aparte creo que es lib externa

class MetodoLagrange:

    def calcularPolinomio(self, ptosX, ptosY) :
        return lagrange(ptosX, ptosY)

    def especializarEnPto(self, numero) :
        return self.calcularPolinomio(self)(numero)

def newtonProgre(listaX, listaY):
	matrizDeCoeficientes = []

	longX = len(listaX)
	longY = len(listaY)

	#Inicializo la matriz
	matrizDeCoeficientes = [[ 0 for i in range(longX+1)] for j in range(longY+1) ] 

	#Seteo las X
	for i in range (longX):
		matrizDeCoeficientes[i][0] = listaX[i]

	#Seteo las Y
	for i in range (longY):
		matrizDeCoeficientes[i][1] = listaY[i]

	#Calculo las diferencias
	for i in range (1,longX):
		k = i - 1
		for j in range (longX - i):
			matrizDeCoeficientes[j][i+1] = (matrizDeCoeficientes[j+1][i] - matrizDeCoeficientes[j][i])/(matrizDeCoeficientes[j+1+k][0] - matrizDeCoeficientes[j][0])

	print(matrizDeCoeficientes)


#main para ir haciendo pruebitas
def main():
	newtonProgre([1,2,3,4],[4,15,40,85])

if __name__ == "__main__":
    main()

#import numpy as np --> np.NombreDeFuncionDeNumpy --> Te deja usar la funcion
#poly1d([1,2],True) genera el polinomio de las raices [1,2]
#poly1d([1,2]) arma el polinomio con esos coeficientes (x+2)(decreciente)