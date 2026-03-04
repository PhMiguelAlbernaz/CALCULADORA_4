class Interface:
	def __init__(self, maq:object):
		self.m:object = maq
	def execute(self):
		print("Qual é o cálculo que quer efetuar? x + - /")
		res:str = input()
		print("Preciso que introduza dois valores:")
		x:float = float(input("x="))
		y:float = float(input("y="))
		if res =="+":
			res = self.m.execute("+",x,y)
			#res = self.m.execute("+"+" "+str(x)+" "+str(y))
			print("O valor da operação somar é:", res)
		# elif res =="/":
		# 	s:object = dividir.Dividir(x,y)
		# 	res = s.executar()
		# 	if type(res)==str:
		# 		print (res)
		# else:
		# 		print("O valor da operação divisão é:",res)
		#
