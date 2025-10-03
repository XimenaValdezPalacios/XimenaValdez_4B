#Practica 5. Patrones de diseño

class Logger:
    #Creamos un atributos de clase donde se guarda la instancia
    _instancia = None

    #_new_ es el metodo qu econtrola la creacion del objeto antes de init. Sirve para asegurarnos
    #de que solo exista una unica instancia de la clase Logger.
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.archivo = open("app.log", "a")
        return cls._instancia
    
    def log(self, mensaje):
        self.archivo.write(mensaje)
        self.archivo.flush()

logger1 = Logger()
logger2 = Logger()

logger1.log("\nInicio de sesion en la aplicacion.")
logger2.log("\nEl usuario se autentico")

print(logger1 is logger2)

class Presidente:
    _instancia = None
    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.historial = []
        return cls._instancia
    
    def accion(self, accion):
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)

p1 = Presidente("Amlo")
p2 = Presidente("Peña Nieto")
p3 = Presidente("Fox")

p1.accion("Firmo decreto")
p2.accion("Visito Espeña")
p3.accion("Aprobo un presupuesto")

print("\nHistorial del presidente")
print(p1.historial)

##1. Que pasaria si eliminamos el sistema de verificacion is cls._instancia is None en el metodo new
##2. Que significa el "True" en p1 is p3 en el contexto del metodo singleton
##3. Es buena idea usae Singleton para todo lo que sea global? Menciona un ejemplo donde no seria recomendable.
