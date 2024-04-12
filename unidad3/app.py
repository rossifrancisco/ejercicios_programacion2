from alumno import Alumno
alumno1 = Alumno("","",0)
alumno2 = Alumno("","",0)
alumno3 = Alumno("","",0)
alumno4 = Alumno("","",0)
alumno5 = Alumno("","",0)

lista = [alumno1, alumno2, alumno3, alumno4, alumno5]
for i in range(5):
    lista[i].nombre = input("ingrese su nombre")
    lista[i].legajo = input("ingrese su legajo")
    lista[i].anioComienzo = input("ingrese su anio de ingreso")

for i in range(5):
    print(lista[i].nombre)
    print(lista[i].legajo)
    print(lista[i].anioComienzo)