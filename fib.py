import threading

# Vetor que armazena os valores calculados
memoria = []
# Vetor de eventos
events = []
# Semaforo para leitura da memaria
semMemoria = threading.BoundedSemaphore(1)


class fib ( threading.Thread ):

	# Sobrescreve o metodo __init__, para possibilitar a passagem de parametros para a thread
	def __init__ ( self, number):
		self.number = number
		threading.Thread.__init__ ( self )

	def run ( self ):
		semMemoria.acquire()
		memAtual = memoria[self.number]
		semMemoria.release()
		if memAtual < 0:
			if(self.number > 1):
				t1 = fib(self.number-1) # inicia a thread do numero anterior
				t2 = fib(self.number-2) # inicia a thread de dois numeros antes
				t2.start() # inicia as threads
				t1.start()
				t1.join() # espera ate que o numero anterior termine de calcular
				semMemoria.acquire()
				memoria[self.number] = memoria[self.number-1]+memoria[self.number-2] # Calcula o fibonacci baseado nos valores em memoria
				semMemoria.release()
			else:
				semMemoria.acquire()
				memoria[self.number] = self.number # para 0 e 1 salva o proprio numero na memoria
				semMemoria.release()


number = 10 # posicao do array do qual se deseja saber o fibonacci

for x in range(number+1): # inicializa a memoria
	memoria.append(-1)

thread = fib(number)
thread.start() # inicia o algoritmo
thread.join() # espera o processo ser concluido
print memoria # exibe o vetor com os valores calculado
print memoria[number] # Exibe o fibonacci na posicao desejada
