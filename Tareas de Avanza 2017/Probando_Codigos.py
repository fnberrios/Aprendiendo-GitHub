from numpy import *
class AddressHolder:



    def __init__(self, calle='', ciudad='', numero='', comuna='',**kwargs):
        super().__init__(**kwargs)
        self.calle = calle
        self.ciudad = ciudad
        self.comuna = comuna
        self.numero = numero
        self.jugueton = array([8, 1, 7, 4, 4])
        self.egoista = array([12, 5, 1, 4, 2])


class Contacto:



    contactos_list = []

    def __init__(self, nombre = '', email = '', **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.email = email
        self.i = 0


        Contacto.contactos_list.append(self)

        if (self.i == 0):
            self.nombre = "FRANCO"



class Cliente(Contacto, AddressHolder):

    def __init__(self, telefono='', **kwargs):
        super().__init__(**kwargs)
        self.telefono = telefono
        self.nuevo = self.jugueton*3






c = Cliente(nombre = 'Juan Perez', email = 'jp@gmail.com', telefono = '23542331',
            calle = 'Pedro de Valdivia', numero = '231', comuna = 'Providencia', ciudad = 'Santiago')

print(c.nombre)
print(c.jugueton)
print(c.nuevo)
print(c.nuevo[0])
comida =0
comida += 1
print(comida)
