# Ejemplo de Arreglos en Python
numeros = [1, 2, 3, 4, 5]

# Acceso a elementos
print("Numeros: ",numeros)

# Agregar un elemento
numeros.append(6)   
print("Numeros: ",numeros)  # Imprime la lista actualizada

# Eliminar un elemento
numeros.remove(3)
print("Numeros: ",numeros)  # Imprime la lista actualizada

# Ejemplo de listas anidadas
Mexico = ["CDMX", "Guadalajara", "Monterrey"]
EstadosUnidos = ["Nueva York", "Los Ángeles", "Chicago"]
Canada = ["Toronto", "Vancouver", "Montreal"]

NorteAmerica = [Mexico, EstadosUnidos, Canada]
print("NorteAmerica:", NorteAmerica)  # Imprime la lista de listas
print("Mexico:", NorteAmerica[0])  # Imprime la lista de Mexico
print("Guadalajara:", NorteAmerica[0][1])  # Imprime Guadalajara