# Conversión de tipos y manejo de cadenas
numero = 123
cadena = str(numero)  # Convertir número a cadena
print("Número como cadena:", cadena)


#Conversion de cadena a entero con try-except
cadena_numero = "hola"
try:
    numero_convertido = int(cadena_numero)  # Convertir cadena a entero
    print("Cadena convertida a número:", numero_convertido)
except ValueError:
    print("Error: La cadena no se puede convertir a número.")

# Concatenación de cadenas
nombre = "Juan"
saludo = "Hola, " + nombre + "!"
print(saludo)

# Formateo de cadenas
edad = 25
print(f"{nombre} tiene {edad} años.")