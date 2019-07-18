class Animales:
    ''' Definimos la clase animales.
    La personalidad puede ser Jugueton o Egoista, segun la personalidad se
    define el mensaje que se transmite al JUGAR o COMER. El multiplicador
    amplifica los parametros de personalidad del animal
     '''
     jugueton = {'sueño': 8, 'juego_ind': 1, 'juego_grup': 7, 'comidas': 4, 'regaloneo': 4}
     egoista = {'sueño': 12, 'juego_ind': 5, 'juego_grup': 1, 'comidas': 4, 'regaloneo': 2}


    def __init__(self, expresion='', nombre='', color='' , sexo='', **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.color = color
        self.sexo = sexo
        self.expresion = expresion ## es un float


    def jugar(self):
        return 0

    def comer(self):
        return 0




class Perros(Animales):
    def __init__(self ):
        super().__init__(**kwargs)

    def ladrar(self):
        return 0




class Gatos(Animales):
    def __init__(self ):
        super().__init__(**kwargs)


    def maullar(self):
        return 0



class SiamePUC(Gatos):
    '''
    personalidad = Egoista, multiplicador = 1 machos y 1.5 hembras
    '''
    def __init__(self ):
        super().__init__(**kwargs)



class GoldenPUC(Perros):
    '''
    personalidad = Juguetona, multiplicador 1.1 machos y 1 hembras
    '''
    def __init__(self ):
        super().__init__(**kwargs)



class PUCTerrier(Perros):
    '''
    personalidad = Egoista, multiplicador = 1.2 machos y 1 hembras
    '''

    def __init__(self ):
        super().__init__(**kwargs)
