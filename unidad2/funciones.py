def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def eliminarDuplicados(lista):
    nuevaLista = []
    nuevaLista = list(set(lista))
    return lista

def soloPares(lista):
    nuevaLista = []
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            nuevaLista.append(lista[i])
    return nuevaLista

def potenciar(lista):
    nuevaLista = []
    nuevaLista = list(map(lambda x: x*x, lista))
    return nuevaLista

def duplicarElementos(lista): #hacer con lambda
    nuevaLista = []
    for i in range(len(lista)):
        nuevaLista.append(lista[i])
        nuevaLista.append(lista[i])
    return nuevaLista

def MayoresQue5(lista):
    nuevaLista = list(filter(lambda x: x>5, lista))
    return nuevaLista

def ordenAscendente(lista):
    nuevaLista = []
    nuevaLista = list(map(lambda x: x, sorted(lista)))
    return nuevaLista

def ordenDiccionariosValorClave(lista, orden): #ejercicio 7 de WhatsApp
    return sorted(lista, key=lambda x: x[orden])

def filtrarPorCondicion(lista, condicion): #ejercicio 8 de WhatsApp
    nuevaLista = list(filter(lambda x: x[0] == condicion, lista))
    return nuevaLista

def ordenSinImportarMayusculasNiMinusculas(lista): #ejercicio 9 de WhatsApp
    nuevaLista = []
    for i in lista:
        nuevaLista.append(str(i).lower())     
    nuevaLista = list(map(lambda x: x, sorted(nuevaLista)))
    return nuevaLista

def filtrarPorSubcadena(lista, subcadena): #ejercicio 10 de WhatsApp
    return list(filter(lambda x: subcadena in x, lista))