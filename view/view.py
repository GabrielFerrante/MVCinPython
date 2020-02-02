from menus import menuPrincipal
from formularios import formCadastroCompra, formRemoverCompra
from paineis import exibirCompras

class View():

	def menu():
		return menuPrincipal()

	def Avisos( mensagem):
		return print("---------------------------"+ mensagem +"--------------------------\n")

	def ChamarCadastroCompra():
		return formCadastroCompra()

	def ChamarExibirCompra(dados):
		exibirCompras(dados)

	def EscolherCompraRemover():
		return formRemoverCompra()
