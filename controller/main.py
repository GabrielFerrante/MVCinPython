# -*- coding: UTF-8 -*-

import sys
import time
sys.path.append('../model/')
sys.path.append('../view/')
from compras import Compras
from view import View
from crudController import cadastrarCompra, ExibindoCompras, removendoCompra

class Controle():
    def __init__(self):
        pass
    def start(self):
        View.Avisos("BEM VINDO GABRIEL!")
        self.menu()

    def exit(self):
        View.Avisos("ATÉ LOGO!!")
        time.sleep(2)
        sys.exit()

    def menu(self):
        while(True):
            escolha =  View.menu()
            if escolha is 1:
                cadastrarCompra()
                continue
            elif escolha is 2:
                removendoCompra()
                continue
            elif escolha is 5:
                View.Avisos("TODAS AS COMPRAS FEITAS!")
                ExibindoCompras()
                continue
            elif escolha is False:
                pass
            elif escolha is 0:
                self.exit()
                pass

if __name__ == "__main__":
    control = Controle()
    control.start()
