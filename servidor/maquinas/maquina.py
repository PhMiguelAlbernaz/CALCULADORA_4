from servidor.operacoes.somar import Somar
from servidor.operacoes.dividir import Dividir
import cliente.interface
class Maquina:
	def __init__(self):
		self.sum = Somar()
		self.div = Dividir()
	# def __init__(cliente.interface.Interface:object interface):
	# 	self.interface:object = interface
	# 	self.somar:object  = servidor.operacoes.somar.Somar()
	# 	self.dividir:object = servidor.operacoes.dividir.Dividir()
	# def exec():
	# 	res = self.interface.exec()
    # 		if res =="+":
    #     	s:object = somar.Somar(x,y)
    #     	res = s.executar(x,y)
    #     	interacao.resultado(res)
    #     print("O valor da operação somar é:", res)
    # elif res =="/":
    #     s:object = dividir.Dividir(x,y)
    #     res = s.executar()
    #     if type(res)==str:
    #         print (res)
    #     else:
    #         print("O valor da operação divisão é:",res)
	# def execute(self,command:str):
	# 	c = command.split()
	# 	# Get the operator
	# 	if c[0] =="+":
	# 		#Call operator
	# 		res = self.sum.execute(float(c[1]),float(c[2]))
	# 	return res

	def execute(self,op:str,op1:float,op2:float):

		# Get the operator
		if op =="+":
			#Call operator
			res = self.sum.execute(op1,op2)
		return res