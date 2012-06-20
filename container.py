import math
import sys

def calcCapacidade(volume):
	arrObjetos = [250, 100, 50, 25, 10, 5, 2, 1]
	arrQuantidade = []

	restante = int(volume)

	for x in arrObjetos:
		arrQuantidade.append(math.floor(restante/x))
		if(math.floor(restante/x) > 0):
			restante = restante%x
	return arrQuantidade

print calcCapacidade(sys.argv[1])
