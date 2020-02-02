import sys
import time
sys.path.append('../model/')
sys.path.append('../view/')
from compras import Compras
from view import View


def cadastrarCompra():
    dicionarioConta = View.ChamarCadastroCompra()
    c = Compras()
    if c.lendoCompra() is 2:
        c.setId(0)
    else:
        c.setId(((len(c.lendoCompra())) + 1) - 1)
    c.setDescricao(dicionarioConta['Descricao'])
    c.setValor(dicionarioConta['Valor'])
    c.setCredor(dicionarioConta['Credor'])
    c.setDataRealizada(dicionarioConta['DataRealizada'])
    if(c.persistindoCompra(c) is True):
        View.Avisos("CADASTRO REALIZADO COM SUCESSO")
    else:
        View.Avisos("ERRO AO PERSISTIR")

def ExibindoCompras():
    c = Compras()
    View.ChamarExibirCompra(c.lendoCompra())
    return True;

def removendoCompra():
    
    c = Compras()
    View.ChamarExibirCompra(c.lendoCompra())
    retorno = View.EscolherCompraRemover()
    if 1 in retorno:
        dados = c.buscandoCompra(retorno[0])
        if dados != False:
            View.Avisos("RESULTADO DA BUSCA!")
            View.ChamarExibirCompra(dados)
        else:
            View.Avisos("Não foi possível buscar compra")
    elif 2 in retorno:
        if c.excluirCompra(retorno[0]) is True:
            View.Avisos("Compra Removida")
    return True
