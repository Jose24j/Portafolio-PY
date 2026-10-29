precio = float(input("Ingrese el precio del producto: "))
if precio >= 100: 
    precio_final = precio * 0.90 
else: 
    precio_final = precio 
print("Precio final:", precio_final)
