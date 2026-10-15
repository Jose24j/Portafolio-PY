edad = int(input("Ingrese la edad del estudiante: "))
tiene_entrada = input("¿El estudiante tiene entrada? (si/no): ").lower()
if edad >= 18 and tiene_entrada == "si":
    print("El estudiante puede ingresar al evento")
else:
    print("El estudiante no puede ingresar al evento")