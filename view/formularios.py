# -*- coding: UTF-8 -*-
from datetime import datetime, date

def formCadastroCompra():
    dicionarioConta = {
        "Id":0,
    	"Nome":"",
    	"Valor":0,
    	"DataRealizada":0,
    	"Credor":""
    }
    print("---------------------------CADASTRO DE CONTA--------------------------\n")
    dicionarioConta['Descricao'] = str(input("Entre com o Descrição da Conta\nDigite: "))
    dicionarioConta['Valor'] = float(input("Entre com o VALOR da Conta\nDigite: "))
    dicionarioConta['Credor'] = str(input("Entre com o CREDOR da Conta\nDigite: "))
    print("ENTRE COM AS DATAS A SEGUIR SEPARANDO ELAS POR ' / '\n")
    dicionarioConta['DataRealizada'] = input("Entre com a DATA DA COMPRA\nDigite: ")
    

    yearR, monthR, dayR = map(int, dicionarioConta['DataRealizada'].split('/'))
    aux = datetime.strptime(str(yearR)+'/'+str(monthR)+'/'+str(dayR),'%d/%m/%Y').date()
    dicionarioConta['DataRealizada'] = aux.strftime('%d/%m/%Y')


    return dicionarioConta

def formRemoverCompra():
    print("---------------------------REMOÇÃO DE COMPRA--------------------------\n")
    print("Entre com a opção:\n1 - Pesquisar compra pela Descrição\n2 - Inserir o ID da compra para remover\n")
    aux = int(input("Digite: \n"))
    if aux is 1:
        des = input("Digite a descrição da compra: \n")
        return [des, 1]
    else:
        cod  = input("Digite o ID da compra: \n")
        return [cod , 2]