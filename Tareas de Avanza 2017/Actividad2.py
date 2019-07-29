from numpy import *
from abc import ABCMeta, abstractmethod
'''la clase animales es una clase abstracta'''

print("ACTIVIDAD 2")

class Animales:
    ''' Definimos la clase animales.
    La personalidad puede ser Jugueton o Egoista, segun la personalidad se
    define el mensaje que se transmite al JUGAR o COMER. El multiplicador
    amplifica los parametros de personalidad del animal

    jugueton = {'sueño': 8, 'juego_ind': 1, 'juego_grup': 7, 'comidas': 4, 'regaloneo': 4}
    egoista = {'sueño': 12, 'juego_ind': 5, 'juego_grup': 1, 'comidas': 4, 'regaloneo': 2}
    '''



    animales_list = []

    def __init__(self, expresion='', nombre='', color='' , **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.color = color
        self.expresion = expresion

        self.jugueton = array([8, 1, 7, 4, 4])
        self.egoista = array([12, 5, 1, 4, 2])

        Animales.animales_list.append(self)


    @abstractmethod
    def jugar(self):
        '''Nunca llegará aquí'''
        return 0

    @abstractmethod
    def comer(self):
        '''Nunca llegará aquí'''
        return 0


    @staticmethod
    def calculos(self):
        sueno = []
        juego_ind = []
        juego_grupal = []
        comidas = 0
        horas_reg = 0

        for elemento in animales_list:

            sueno.append(elemento.estadistica[0])
            juego_ind.append(elemento.estadistica[1])
            juego_grupal.append(elemento.estadistica[2])
            comidas += elemento.estadistica[3]
            horas_reg += elemento.estadistica[4]

        print("Horas de sueño minimas: {}".format(min(sueno)))
        print("Horas de juego individual mínimas: {}".format(min(juego_ind)))
        print("Horas de juego grupal máximo: {}".formart(max(juego_grupal)))
        print("Cantidad de Comidas Diarias: {}".format(comidas))
        print("Cantidad de Horas de regaloneo: {}",format(horas_reg))



class Perros(Animales):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def ladrar(self):
        print("Guau!! Guau!!")

    def jugar(self):
        print("Tírame la pelota :)")

    def comer(self):
        print("Mami :) Quiero comeeeerr!!")



class Gatos(Animales):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def maullar(self):
        print("Miauuu!! Miauuu!")

    def jugar(self):
        print("Humano, ahora, juguemos.")

    def comer(self):
        print("El pellet es horrible. Dame comida en lata")



class SiamePUC(Gatos):
    '''
    personalidad = Egoista, multiplicador = 1 machos y 1.5 hembras
    '''

    def __init__(self, sexo='', **kwargs):
        super().__init__(**kwargs)
        self.sexo = sexo.lower()


        if (self.sexo == "hembra"):
            self.estadistica = self.egoista*1.5

        elif (self.sexo == "macho"):
            self.estadistica = self.egoista*1




class GoldenPUC(Perros):
    '''
    personalidad = Juguetona, multiplicador 1.1 machos y 1 hembras
    '''
    def __init__(self, sexo='', **kwargs):
        super().__init__(**kwargs)
        self.sexo = sexo.lower()

        if (self.sexo == "hembra"):
            self.estadistica = self.jugueton

        elif (self.sexo == "macho"):
            self.estadistica = self.jugueton*1.1


class PUCTerrier(Perros):
    '''
    personalidad = Egoista, multiplicador = 1.2 machos y 1 hembras
    '''

    def __init__(self, sexo='', **kwargs):
        super().__init__(**kwargs)
        self.sexo = sexo.lower()


        if (self.sexo == "hembra"):
            self.estadistica = self.egoista*1

        elif (self.sexo == "macho"):
            self.estadistica = self.egoista*1.2

##########################################################################


uno = SiamePUC(expresion=0.5, nombre="Mara", color="Blanco", sexo="Hembra")
print(uno.sexo)
print(uno.estadistica)
uno.calculos
