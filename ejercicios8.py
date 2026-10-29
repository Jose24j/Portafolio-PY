nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) /3
if promedio >= 71:
    print("El estudiante:", nombre, "con edad de", edad, "años", "ha aprobado con un promedio de:", promedio)
else:
    print("El estudiante:", nombre, "con edad de", edad, "años", "ha reprobado con un promedio de:", promedio)