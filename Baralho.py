class Carta:
    __naipe = None
    __valor = None
    __naipes_validos = ["copas", "ouros", "paus", "espadas"]
    __valores_validos = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "k"]

    def __init__(self, naipe = None, valor = None):
        if naipe in self.__naipes_validos:
            self.__naipe = naipe

        if valor in self.__valores_validos:
            self.__valor = valor    
            

    @property
    def naipe(self):
        return self.__naipe

    @naipe.setter
    def naipe(self, naipe):
        if self.__naipe is None:
            if naipe in self.__naipes_validos:
                self.__naipe = naipe

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if self.__valor is None:
            if valor in self.__valor_validos:
                self.__valor = valor

import random

class Baralho:
    __cartas = []

    def __init__(self):
        carta0 = Carta()
        cartas = []
        for naipe in carta0._Carta__naipes_validos:
            for valor in carta0._Carta__valores_validos:
                carta = Carta(naipe, valor)
                cartas.append(carta)
        self.__cartas = cartas

    @property
    def cartas(self):
        return self.__cartas

    def embaralhar(self):
        random.shuffle(self.__cartas)
        return self.__cartas

baralho1 = Baralho()
baralho1.embaralhar()
cartas = baralho1.cartas
for carta in cartas:
    print(carta.valor, carta.naipe)
