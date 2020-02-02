# -*- coding: UTF-8 -*-
def exibirCompras(dados):
	#print(dados)
	try:
		if dados:
			print("""-------ID   | Descrição                             | VALOR          | CREDOR                | REALIZADA       \n""")
			for item in dados:
			#print(item)
				print("-------",str(item),"  |",dados[str(item)]['Dados']['Descricao']," | ","%.2f" % dados[str(item)]['Dados']['Valor']," | ",dados[str(item)]['Dados']['Credor']," | ",dados[str(item)]['Dados']['DataRealizada'],"\n")
		else:
			print("Não existe dados cadastrados")
	except Exception as e:
		print("Não foi possível exibir Compras")
	

