# Practica 1 Clase Objetos y Atributos
#una clase es una plantilla o un molde
#que define como sera un objeto.

class persona:
    def __init__(self, nombre, edad): #Constructor de una clase
      self.nombre = nombre
      self.edad = edad

    def presentarse(self):
      print(f"Hola mi nombre es {self.nombre}")

    def cumplir_anios(self  ):
       self.edad += 1
       print (f"{self.nombre} ahora tiene {self.edad} años")

#un objeto es una instancia creada a partir de una clase

estudiante1 = persona("Ximena", 19) #crecaion de un objeto
estudiante2 = persona("Cesar", 19)

estudiante1.presentarse()
estudiante2.presentarse()

estudiante1.cumplir_anios()
estudiante2.cumplir_anios()
#Paso 1. Agrega un metodo cumplir_anios() que aumente en 1 la edad

#INSTANCIA:
# Cada objeto creado de una clase es una instancia
# Podemos tener varias instancias que coexistan con sus propios datos
# Objeto = Instancia de clase
# Cada vez que se crea un objeto con (lasel) se obtiene un isnatncia dependiente
# Cada instancia tiene sus propios datos aunque vengan en la misma clase

#ABSTRACCION:
# Representar solo lo importante del mundo real ocultando detalles innecesarios

class automovil:
    def __init__(self, marca):
      self.marca = marca

    def arrancar(self):
       print(f"{self.marca} arrancó")

#Crear un objeto auto y asiganr una marca
auto1 = automovil("TOYOTA")
auto1.arrancar()

#ABSTRACCIÓN:
# Nos centramos solo en lo que importa (acción), que es arrancar el automovil ocultando detalles 
# internoa: como motor, transmisión, tipo_combustible.
# Enfoque solo en la acción del objeto.
# Objetivo es hacer el código mas limpio y facil de usar

#Práctica 1.2 
# Crear una clase mascotas
# Agregar minimo 4 atributos
# Definir al menos 4 metodos 
# Crear 2 instancias de la clase 
# Llamar los metodos y aplicar abstracción. (Agregar un atributo innecesario)

class mascotas:
    def __init__(self, nombre, especie, edad, color, dueño):
      self.nombre = nombre
      self.especie = especie
      self.edad = edad
      self.color = color
      self.dueño = dueño

    def presentarse(self):
       print(f"Hola, soy {self.nombre}, una {self.especie} de color {self.color}.")
    
    def edad_act(self):
       print(f"La edad actual de la mascota es de: {self.edad}")

    def cumplir_anios(self):
       self.edad += 1
       print(f"{self.nombre} cumplira {self.edad} años")

    def dueno_masc(self):
       print(f"El dueño de {self.nombre} es: {self.dueño}")


mascota1 = mascotas ("Gord", "Chihuahua", 4, "negro", "Genesis")
mascota2 = mascotas ("Roky", "Pastor Aleman", 3, "cafe y blanco", "Ximena")


mascota1.presentarse()
mascota1.edad_act()
mascota1.cumplir_anios()
mascota1.dueno_masc()


mascota2.presentarse()
mascota2.edad_act()
mascota2.cumplir_anios()
mascota2.dueno_masc()
