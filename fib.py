import threading

# Vetor que armazena os valores calculados
memoria = []
# Vetor de eventos
events = []
# Semáforo para leitura da memória
semMemoria = threading.BoundedSemaphore(1)


class fib ( threading.Thread ):

	# Sobrescreve o método __init__, para possibilitar a passagem de parâmetros para a thread
	def __init__ ( self, number):
		self.number = number
		threading.Thread.__init__ ( self )

	def run ( self ):
		semMemoria.acquire()
		lenMem = len(memoria)
		semMemoria.release()
		
		if(self.number > 1):
			fib(self.number-1).start() # inicia a thread to número anterior
			events[self.number-1].wait() # Espera até que a thread termine de calcular
			semMemoria.acquire()
			memoria.append(memoria[self.number-1]+memoria[self.number-2]) # Calcula o fibonacci baseado nos valores em memória
			semMemoria.release()
		else:
			if self.number == 1:
				fib(self.number-1).start() # inicia o fibonacci de 0
				events[self.number-1].wait() # Espera terminar
			semMemoria.acquire()
			memoria.append(self.number) # para 0 e 1 salva o próprio número na memória
			semMemoria.release()

		events[self.number].set() # dispara o evento, dizendo que a thread está concluida
		

for x in range(11):
	events.append(threading.Event()) # inicializa o vetor de eventos

fib(10).start() # inicia o algoritmo
events[10].wait() # espera até que a thread inicial esteja completa
print memoria # exibe o vetor com os valores calculado
