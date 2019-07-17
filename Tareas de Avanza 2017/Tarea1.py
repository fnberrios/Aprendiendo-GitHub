class Automotora():
    def __init__(self, nombre): # no se requiere crear sucursales como entrada de la clases, pues es una variable interna
        self.nombre = nombre
        self.sucursales = [] # LISTA EN LA QUE SE AGREGARAN LAS SUCURSALES

    def agregar_sucursal(self, nueva_sucursal):
        self.sucursales.append(nueva_sucursal)


class Sucursal():
    def __init__(self,nombre):
        self.nombre = nombre
        self.autos_usados = []
        self.autos_nuevos = []
        self.autos = []

    def agregar_auto(self,nuevo_auto):
        self.autos.append(nuevo_auto)


        if (nuevo_auto.estado == "nuevo"):
            self.autos_nuevos.append(nuevo_auto)
        elif (nuevo_auto.estado == "usado"):
            self.autos_usados.append(nuevo_auto)
        else:
            print("ERROR AL INGRESAR EL AUTO")

class Automovil():
    def __init__(self, _id, marca, ano, modelo, transmicion, precio, estado, dueno):
        self._id = _id
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.transmicion = transmicion # AT/MT
        self.precio = precio
        self.estado = estado # NUEVO/USADO
        self.dueno = dueno #  SERA UNA LISTA CON LOS SGTES DATOS; nombre, rut, telefono y correo, EN ESE ORDEN

import sys
class Menu:
    def __init__(self, automotora):
        self.automotora = automotora
        self.opciones = {
                        "1": self.busqueda,
                        "2": self.cambiar_precio,
                        "3": self.salir,
                        "4": self.mostrar
                        }

    def display_menu(self):
        print("""
            Menu:
                1: Búsqueda de Automóviles
                2: Cambiar Precio de un Automóvil (Solo Trabajadores)
                3: Salir
                4: Mostrar todos los autos
            """)



    def run(self):

        while True:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()#aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))


    def busqueda(self):
        print("Ingrese los datos de la busqueda en minuscula y sin acentos \n")

        ano_min = int(input("Automóviles desde el año: "))
        ano_max = int(input("Automóviles hasta el año: "))
        precio_min = int(input("Precios mayores a: "))
        precio_max = int(input("Precios menores a: "))
        marca = input("Marca del automóvil: ")
        transmicion = input("Transmición Automatica (AT) o Manual (MT): ")
        estado = input("Automóvil Nuevo o Usado: ")

        for sucursal_movil in self.automotora.sucursales:
            print("Revisando Sucursal {0}".format(sucursal_movil.nombre))
            for automovil_movil in sucursal_movil.autos:

                if (automovil_movil.estado == estado):
                    if (automovil_movil.transmicion == transmicion):
                        if (automovil_movil.marca == marca):
                            if (( int(automovil_movil.precio) <= precio_min) and ( int(automovil_movil.precio) <= precio_max)):
                                if (( int(utomovil_movil.ano) <= ano_min) and ( int(automovil_movil.ano) <= ano_max)):
                                    print("si")
                                    print(""" Estado: {0} | Transmción: {1} | Marca: {2} | Dueño: {3} | Año: {4}                                            Precio:
                                              """.format(automovil_movil.estado,automovil_movil.transmicion,automovil_movil.marca,
                                                        automovil_movil.dueno,automovil_movil.ano))


    def cambiar_precio(self): ## 1. EL PRECIO DEBE SER DIVISIBLE POR $500.000
        error = 0
        cantidad_de_vehiculos = 0
        id_por_cambiar = input("Ingrese el ID del auto que desea modificar el precio: ")
        precio_nuevo = input("Nuevo precio del vehículo: ")

        for sucursal_movil in automotora.sucursales:
            for id_del_auto in sucursal_movil.autos:

                cantidad_de_vehiculos += 1
                if (id_por_cambiar == id_del_auto._id):
                    id_del_auto.precio = precio_nuevo
                    error += 1
                    print("El precio se cambió con éxito")

        print("En la Automotora existe un total de {0} vehículos".format(cantidad_de_vehiculos))

        if (error == 0):
            print("ERROR, vehículo no encontrado")


    def mostrar(self):
        for sucursal_movil in self.automotora.sucursales:
            print("Revisando Sucursal {0}".format(sucursal_movil.nombre))
            for automovil_movil in sucursal_movil.autos:
                print(""" Estado: {0} | Transmción: {1} | Marca: {2} | Dueño: {3}
                             Año: {4} | Precio {5}
                """.format(automovil_movil.estado,automovil_movil.transmicion,automovil_movil.marca,
                               automovil_movil.dueno,automovil_movil.ano,automovil_movil.precio))


    def salir(self):
        print("Gracias por usar nuestro Servicio")
        sys.exit(0)


s1_n1 = Automovil("1","Lexus","2010","z1","AT","300000","nuevo", [])
s1_n2 = Automovil("2","Toyota","2011","Corola","MT","100000","nuevo", [])
s1_n3 = Automovil("3","Toyota","2011","Corola","MT","100000","nuevo", [])
s1_u1 = Automovil("4","Toyota","2011","Corola","MT","100000","usado", [])
s1_u2 = Automovil("5","Toyota","2011","Corola","MT","100000","usado", [])
s1_u3 = Automovil("6","Toyota","2011","Corola","MT","100000","usado", [])

s2_n1 = Automovil("7","Toyota","2011","Corola","MT","100000","nuevo", [])
s2_n2 = Automovil("8","Toyota","2011","Corola","MT","100000","nuevo", [])
s2_n3 = Automovil("9","Toyota","2011","Corola","MT","100000","nuevo", [])
s2_u1 = Automovil("10","Toyota","2011","Corola","MT","100000","usado", [])
s2_u2 = Automovil("11","Nissan","2012","Skyline","AT","700000","usado", [])
s2_u3 = Automovil("12","Audi","2015","R8","AT","3000000","usado", [])

s1 = Sucursal("1")
s2 = Sucursal("2")

s1.agregar_auto(s1_n1)
s1.agregar_auto(s1_n2)
s1.agregar_auto(s1_n3)
s1.agregar_auto(s1_u1)
s1.agregar_auto(s1_u2)
s1.agregar_auto(s1_u3)

s2.agregar_auto(s2_n1)
s2.agregar_auto(s2_n2)
s2.agregar_auto(s2_n3)
s2.agregar_auto(s2_u1)
s2.agregar_auto(s2_u2)
s2.agregar_auto(s2_u3)



automotora_creada = Automotora("Automóviles Mavrakis")
automotora_creada.agregar_sucursal(s1)
automotora_creada.agregar_sucursal(s2)


if __name__ == "__main__":#esto es para que corra en la consola
    Menu(automotora_creada).run()
