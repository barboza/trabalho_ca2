import math
import sys

# Calcula o menor número de objetos (tamanhos definidos no array) que cabem em um container
# basta rodar o script mandando a capacidade como parâmetro
# ex: python container.py 5476

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
