# -*- coding: UTF-8 -*-
def menuPrincipal():
	try:
		return int(input("1 - Cadastrar Compra\n2 - Removendo Compra\n5 - Listar compras\nDigite a opção: "))
	except Exception as e:
		return False
