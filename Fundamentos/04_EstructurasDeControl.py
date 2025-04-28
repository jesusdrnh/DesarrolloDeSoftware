# Ejemplo de estructuras de control en Python
numero = 5

# Estructura condicional
if numero > 0:
    print("El numero es positivo.")
else:
    print("El numero es negativo o cero.")

switch = "tres"
match numero:
    case 1:
        print("Uno")
    case '2':
        print("Dos")
    case "tres":
        print("Tres")
    case _:
        print("numero no valido")

# Bucle for
for i in range(3):
    print(f"Iteracion {i} de 3")
    print("Iteracion ", i, "de 3")

# Estructura de control con break y continue    
for i in range(10):
    if i == 2:
        continue  # Salta la iteración actual
    if i == 4:
        break  # Sale del bucle
    print(f"Valor: {i}")

# Bucle while
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

#Bucle do while
# No existe en Python, pero se puede simular con un bucle while
contador = 0
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 3:
        break  # Sale del bucle