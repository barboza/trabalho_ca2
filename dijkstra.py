def readFile(filename):
	array = [[],[],[]]
	f = open(filename,'r')
	
	lines = f.readlines()
	index = -1
	for line in lines:
		line = line.rstrip('\n')		
		if line.startswith('#'):
			index += 1
		else:
			
			if index < 2:
				line = line.split(',')
			else:
				line = line.split(';')
			array[index].append(line)
	return array


def abertos(matriz):
	count = 0
	for x in matriz[3]:
		if(x == 0):
			count += 1
	return count

def getMenorEstimativa(matriz):
	menor = 100000
	for x in range(len(matriz[1])):
		if matriz[1][x] < menor && matriz[3][x] == 0
			menor = x
	return menor


def dijkstra(origem, destino):
	vertices = data[0]
	arestas = data[1]

	matriz = []
	matriz.append(vertices)
	matriz.append([100000]*len(vertices))
	matriz.append([-1]*len(vertices))
	matriz.append([0]*len(vertices))

	for x in range(len(vertices)):
		if(vertices[x] == origem):
			origem = x
		if(vertices[x] == destino):
			destino = x

	matriz[1][origem] = 0
	while abertos(matriz) > 0:
		 nodoAtual = getMenorEstimativa(matriz)
		 matriz[3][nodoAtual] = 1
		 




data = readFile('teste.txt')

dijkstra("taquara","igrejinha")
