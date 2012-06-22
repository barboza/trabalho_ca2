import sys

#percorre o arquivo e gera um array
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
			if index == 1:
				line = line.split(',')
				for i in range(len(line)):
					line[i] = line[i].strip() # retira espacos antes e depois
			if index == 2:
				line = line.split(';')
				for i in range(len(line)):
					line[i] = line[i].strip() # retira espacos antes e depois
			array[index].append(line)
	return array

# Verifica quantos nodos nao calculados ainda existem na matriz
def abertos(matriz):
	count = 0
	for x in matriz[3]:
		if(x == 0):
			count += 1
	return count

# retorna o indice do nodo aberto com a menor distancia estimada ate a origem
def getMenorEstimativa(matriz):
	menor = 100000
	indexMenor = -1
	for x in range(len(matriz[1])):
		if matriz[1][x] < menor and matriz[3][x] == 0:
			menor = matriz[1][x]
			indexMenor = x
	return indexMenor

# retorna a menor distancia estimada ate a origem, ou "infinito" caso nao exista rota
def getEstimativa(origem, destino):
	origem = data[0][origem]
	destino = data[0][destino]

	menor = 100000

	for aresta in data[1]:
		if (aresta[0] == origem and aresta[1] == destino) or (aresta[1] == origem and aresta[0] == destino):
			if int(aresta[2]) < menor:
				menor = int(aresta[2])

	return menor


# retorna os nodos que possuem conexao com o nodo requisitado, ou [] caso nao exista nenhuma conexao
def getVizinhos(nodo):
	nomeNodo = data[0][nodo]
	vizinhos = []
	indexVizinhos = []

	for x in range(len(data[1])):
		if data[1][x][0] == nomeNodo:
			vizinhos.append(data[1][x][1])
		if data[1][x][1] == nomeNodo:
			vizinhos.append(data[1][x][0])

	for y in vizinhos:
		for i in range(len(data[0])):
			if data[0][i] == y:
				indexVizinhos.append(i)
	return indexVizinhos


# retorna uma lista com o caminho mais curto da origem ao destino (nao inclui o destino)
def dijkstra(origem, destino):
	vertices = data[0]
	arestas = data[1]

	# inicializa a matriz para calculo
	matriz = []
	matriz.append(vertices) # lista dos vertices
	matriz.append([100000]*len(vertices)) # lista das estimativas da origem ate o vertice
	matriz.append([-1]*len(vertices)) # nodo predecessor do vertice (-1 caso nao exista)
	matriz.append([0]*len(vertices)) # flag indicando se o nodo esta aberto ou fechado

	# transforma o nome das cidades no indice (ex: 'taquara'->1)
	for x in range(len(vertices)):
		if(vertices[x] == origem):
			origem = x
		if(vertices[x] == destino):
			destino = x

	matriz[1][origem] = 0 # fecha o nodo de origem
	while abertos(matriz) > 0:
		 nodoAtual = getMenorEstimativa(matriz)
		 if(nodoAtual == -1): # quebra o while caso alguma cidade nao possua conexoes (continuara aberta porem sem estimativa)
		 	break
		 matriz[3][nodoAtual] = 1 # fecha o nodo atual
		 vizinhos = getVizinhos(nodoAtual)
		 if len(vizinhos) > 0: # se possuir vizinhos
			 for vizinho in vizinhos:
			 	estimativa = getEstimativa(nodoAtual,vizinho) # recupera estimativa de cada vizinho
			 	if matriz[1][vizinho] > (matriz[1][nodoAtual] + estimativa): # define estimativa se a estimativa for menor que a anterior
			 		matriz[1][vizinho] = matriz[1][nodoAtual] + estimativa
			 		matriz[2][vizinho] =  nodoAtual # define o predecessor como sendo o nodo atual
	if matriz[2][destino] == -1: # retorna vazio caso nao haja conexoes com o destino
		return []
	else: # senao gera uma lista com a rota ate o destino
		path = []
		atual = destino
		while(atual != origem): # gera lista com os nomes das cidades
			atual = matriz[2][atual]
			path.append(atual)
		path.reverse()
		return path

data = readFile(sys.argv[1])

path = []
pathString = ''
data[2] = data[2][0]
invalida = 0
if len(data[2]) > 1:	
	for x in range(len(data[2])-1):
		parcialPath = dijkstra(data[2][x],data[2][x+1])
		if len(parcialPath) > 0:
			path += parcialPath
		else:
			invalida = 1
	for y in path:
		pathString += data[0][y]+'->'
	pathString += data[2].pop()
if invalida == 0:
	print pathString
else:
	print "Rota Invalida"

