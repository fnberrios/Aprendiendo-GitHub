from data_A3 import * # para importar los datos
from random import randint, uniform,random
from collections import namedtuple
from collections import deque


def crear_oraciones(cantidad_oraciones):

    sujeto = (articulos, sustantivos)
    verbo = (verbosN, verbosV)
    predicado = (adjs, ("", sustantivos))

    lista_oraciones = []  # CREAMOS PILA DONDE GUARDAREMOS LAS ORACIONES
    palabras_anteriores = deque()
    i = 1
    while (cantidad_oraciones != 0):
        #str.capitalize() # La primera letra mayuscula

        articulo_selec = articulos[randint(0, len(articulos)-1)]
        while (len(palabras_anteriores) != 0 and articulo_selec == palabras_anteriores[0]):
            articulo_selec = articulos[randint(0, len(articulos)-1)]

        if (i != 1):
            palabras_anteriores.popleft()  # boraamos el primer articulo
        palabras_anteriores.append(articulo_selec)  # agregamos el ultimo

        sustantivo_selec = sustantivos[randint(0, len(sustantivos)-1)]
        while (sustantivo_selec == palabras_anteriores[0]):
            sustantivo_selec = sustantivos[randint(0, len(articulos)-1)]
        if (i != 1):
            palabras_anteriores.popleft()
        palabras_anteriores.append(articulo_selec)

        correspondencia_VyP = randint(0,1)
        verbo_azar = verbo[correspondencia_VyP]
        verbo_selec = verbo_azar[randint(0, len(verbo_azar)-1)]
        while (verbo_selec == palabras_anteriores[0]):
            verbo_selec = verbo_azar[randint(0, len(verbo_azar)-1)]
        if (i != 1):
            palabras_anteriores.popleft()
        palabras_anteriores.append(verbo_selec)

        if (correspondencia_VyP == 0):
            adjs_selec = adjs[randint(0, len(adjs)-1)]
            while(adjs_selec == palabras_anteriores[0]):
                adjs_selec = adjs[randint(0, len(adjs)-1)]
            if (i != 1):
                palabras_anteriores.popleft()
            palabras_anteriores.append(adjs_selec)

        else:
            adjs_azar = randint(0, 1)
            if(adjs_azar == 1):
                adjs_selec = sustantivos[randint(0, len(sujeto)-1)]
            else:
                adjs_selec = ""

            while (palabras_anteriores[0] == adjs_selec):
                adjs_azar = randint(0, 1)
                if(adjs_azar == 1):
                    adjs_selec = sustantivos[randint(0, len(sujeto)-1)]
                else:
                    adjs_selec = ""
            if (i != 1):
                palabras_anteriores.popleft()
            palabras_anteriores.append(adjs_selec)

        i += 1
        nueva_oracion = articulo_selec + " " + sustantivo_selec + " "
        nueva_oracion = nueva_oracion + verbo_selec + " " + adjs_selec + "."
        nueva_oracion = nueva_oracion.capitalize()
        lista_oraciones.append(nueva_oracion)
        cantidad_oraciones -= 1
    return lista_oraciones

print(crear_oraciones(20))
