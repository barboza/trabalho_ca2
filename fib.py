import threading

memoria = []
events = []
semMemoria = threading.BoundedSemaphore(1)

class fib ( threading.Thread ):

	def __init__ ( self, number):
		self.number = number
		threading.Thread.__init__ ( self )

	def run ( self ):
		semMemoria.acquire()
		lenMem = len(memoria)
		semMemoria.release()
		if lenMem < self.number:
			print self.number
			if(self.number > 1):
				fib(self.number-1).start()
				fib(self.number-2).start()
				events[self.number-1].wait()
				events[self.number-2].wait()
				semMemoria.acquire()
				print "num"
				print self.number
				memoria.append(memoria[self.number-1]+memoria[self.number-2])
				semMemoria.release()
			else:
				semMemoria.acquire()
				memoria.append(self.number)
				semMemoria.release()
		print self.number
		events[self.number].set();
		semMemoria.acquire()
		print memoria
		semMemoria.release()
		

for x in range(11):
	events.append(threading.Event())
print events
fib(10).start()
events[9].wait()
print memoria[9]
