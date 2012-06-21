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
		lenMem = len(memoria)
		semMemoria.release()
		
		if(self.number > 1):
			fib(self.number-1).start() # inicia a thread to numero anterior
			events[self.number-1].wait() # Espera ate que a thread termine de calcular
			semMemoria.acquire()
			memoria.append(memoria[self.number-1]+memoria[self.number-2]) # Calcula o fibonacci baseado nos valores em memoria
			semMemoria.release()
		else:
			if self.number == 1:
				fib(self.number-1).start() # inicia o fibonacci de 0
				events[self.number-1].wait() # Espera terminar
			semMemoria.acquire()
			memoria.append(self.number) # para 0 e 1 salva o proprio numero na memoria
			semMemoria.release()

		events[self.number].set() # dispara o evento, dizendo que a thread esta concluida
		
number = 10 # posicao do array do qual se deseja saber o fibonacci

for x in range(number+1): # [0] ate [10]
	events.append(threading.Event()) # inicializa o vetor de eventos

fib(number).start() # inicia o algoritmo
events[number].wait() # espera ate que a thread inicial esteja completa
print memoria # exibe o vetor com os valores calculado
print memoria[number] # Exibe o fibonacci na posição desejada
