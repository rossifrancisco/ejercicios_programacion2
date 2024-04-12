from funciones import *

print("menu principal")
print("")
print("1 sumar")
print("2 restar")
print("3 multiplicar")
print("4 dividir")
print("5 eliminar duplicados")
print("6 eliminar impares")
print("7 potenciar lista")
print("8 duplicar lista")
print("9 mayores que cinco")
print("10 orden ascendente")
print("11 ordenar cadenas por longitud ascendente")
print("12 eliminar pares")
print("13 eliminar palabras que empiecen con 'a'")
print("14 ordenar Ordenar una lista de tuplas por el segundo elemento")
print("15 Filtrar números primos de una lista")
print("16 Ordenar una lista de diccionarios por el valor de una clave específica")
print("17 Filtrar elementos que cumplen una condición específica")
print("18 Ordenar una lista de cadenas ignorando mayúsculas y minúsculas")
print("19 Filtrar elementos que contienen una subcadena específica")
print("0 salir")
print("")
opc = int(input("ingrese una opcion "))
while (opc<0 or opc>19):
    print("")
    opc=int(input("ingrese una opcion valida "))

if opc==1:
    num1 = int(input("ingrese primer numero "))
    num2 = int(input("ingrese segundo numero "))
    print(sumar(num1, num2))

elif opc==2:
    num1 = int(input("ingrese primer numero "))
    num2 = int(input("ingrese segundo numero "))
    print(restar(num1, num2))

elif opc==3:
    num1 = int(input("ingrese primer numero "))
    num2 = int(input("ingrese segundo numero "))
    print(multiplicar(num1, num2))

elif opc==4:
    num1 = int(input("ingrese primer numero "))
    num2 = int(input("ingrese segundo numero "))
    print(dividir(num1, num2))

elif opc==5:
    print(eliminarDuplicados([1,1,1,2,3,2,3,5,4,5]))

elif opc==6:
    print(soloPares([1,2,3,4,5,6,7,8,9]))

elif opc==7:
    print(potenciar([1,2,3,4,5]))

elif opc==8:
    print(duplicarElementos([1,2,3,4,5]))

elif opc==9:
    print(MayoresQue5([1,2,3,4,5,6,7,8,9]))

elif opc==10:
    print(ordenAscendente([5,4,3,2,1]))

elif opc==11:
    print("esta es la opcion 11")

elif opc==12:
    print("esta es la opcion 12")

elif opc==13:
    print("esta es la opcion 13")

elif opc==14:
    print("esta es la opcion 14")

elif opc==15:
    print("esta es la opcion 15")

elif opc==16: #ejercicio 7 de WhatsApp
    diccionario1 = {
        "auto":2,
        "precio":2
    }
    diccionario2 = {
        "auto":1,
        "precio":3
    }
    diccionario3 = {
        "auto":3,
        "precio":1
    }
    listaDiccionarios = [diccionario1, diccionario2, diccionario3]

    print("1 para ordenar por precio")
    print("2 para ordenar por auto")
    print("")
    opc2 = int(input("ingrese una opcion "))
    while (opc2<1 or opc2>2):
        print("")
        opc2=int(input("ingrese una opcion valida "))
    if opc2==1:
        orden = "precio"
    elif opc2==2:
        orden = "auto"
    else:
        print("error")

    print(ordenDiccionariosValorClave(listaDiccionarios, orden))

elif opc==17: #ejercicio 8 de WhatsApp
    lista = ["casa", "arbol", "manzana", "araña", "lluvia", "agua", "zapato"]
    condicion = input("ingrese una letra para buscar palabra por inicial: ")
    print(filtrarPorCondicion(lista, condicion))

elif opc==18: #ejercicio 9 de WhatsApp
    lista = ["casa", "arbol", "Manzana", "Araña", "Lluvia", "agua", "Zapato"]
    print(ordenSinImportarMayusculasNiMinusculas(lista))

elif opc==19: #ejercicio 10 de WhatsApp
    lista = ["casa", "arbol", "manzana", "araña", "lluvia", "agua", "Zapato"]
    subcadena = input("ingrese una subcadena a buscar: ")
    print(filtrarPorSubcadena(lista, subcadena))

elif opc==0:
    print("hasta luego")

else:
    print("error")