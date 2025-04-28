# Ejemplo de clases y objetos en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Crear un objeto
persona = Persona("Juan", 30)
print(persona.saludar())

#Herencia en Python
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def saludar(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

# Crear un objeto de la clase Estudiante
estudiante = Estudiante("Ana", 22, "Ingeniería")
print(estudiante.saludar())