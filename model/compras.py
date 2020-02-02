import json

class Compras():
    def __init__(self):
        pass
    #Set e Get

    def setId(self, PK):
        self.__id = PK
    def getId(self):
        return self.__id

    def setDescricao(self,nome):
    	self.__nome = nome

    def getDescricao(self):
    	return self.__nome

    def setValor(self,valor):
    	self.__valor = valor

    def getValor(self):
    	return self.__valor
    
    def setCredor(self,credor):
        self.__credor = credor

    def getCredor(self):
        return self.__credor

    def setDataRealizada(self, data):
        self.__dataR = data

    def getDataRealizada(self):
        return self.__dataR

    #Métodos
    def gravandoDados(self, dicListContas):
        with open('../model/COMPRAS.json', 'w', encoding='utf-8') as f:
                json.dump(dicListContas, f, ensure_ascii=False, indent=4)
        return True
    def persistindoCompra(self, compra):
        try:
            jsonDic = {
                compra.getId():{
                    'Dados':{
                        'Descricao':compra.getDescricao(),
                        'Valor': compra.getValor(),
                        'Credor': compra.getCredor(),
                        'DataRealizada':compra.getDataRealizada()
                    }
                }
            }
            if(self.lendoCompra()==2):
                if(self.gravandoDados(jsonDic)):
                    return True
                else:
                    return False
            else:
                dicListCompras = self.lendoCompra()
                dicListCompras[compra.getId()] = jsonDic[compra.getId()]
                if(self.gravandoDados(dicListCompras)):
                    return True
                else:
                    return False
                    
        except Exception as e:
            raise e
        
        
    def lendoCompra(self):
        try:
            with open('../model/COMPRAS.json') as json_file:
                data = json.load(json_file)
            if(data is not None):
                return data
            else:
                return 1
        except IOError:
            print('Arquivo não encontrado!')
            return 2

    def excluirCompra(self,id):
        try:
            dicListCompras = self.lendoCompra()
            if id in dicListCompras:
                del dicListCompras[id]
            self.gravandoDados(dicListCompras)
            return True
        except Exception as e:
            return False


    def buscandoCompra(self, descricao):
        try:
            dicListCompras = self.lendoCompra()
            i = 0
            result = {}
            for item in dicListCompras:
                if dicListCompras[item]['Dados']['Descricao'] == descricao:
                    result[str(i)] = dicListCompras[item]
                i = i+1
            return result
        except Exception as e:
            return False