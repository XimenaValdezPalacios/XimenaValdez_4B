import os
os.system('cls')
#Practica 3. Introducción al polimorfismo
#Simular un sistema de cobro con multiples opciones de pago

class pago_tarjeta:
    def procesar_pago(self,cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta bancaria"
    
class transferencia:
    def procesar_pago(self, cantidad):
        return f"Procesar pago con transeferencia por la cantidad de ${cantidad}"
    
class deposito:
    def procesar_pago(self, cantidad):
        return f"Procesando pago por medio deposito en ventanilla por la cantidad de ${cantidad}"
    
class paypal:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} por medio de paypal"
    
#Instancia
metodos_pago = [pago_tarjeta(), transferencia(), deposito(), paypal()]

#ACTIVIDAD: PROCESAR PAGO CON DIFERENTES CANTIDADES EN CADA UNA DE LAS FORMAS 
#DE PAGO, EJEMPLO: 100 CON TARJETA, 500 CON TRANSFERENCIA, 2000 CON PAYPAL, 
#400 CON DEPOSITO.

pago1 = pago_tarjeta()
pago2 = transferencia()
pago3 = deposito()
pago4 = paypal()

#Polimorfismo: Mismo metodo con diferentes objetos.
print(pago1.procesar_pago(100))
print(pago1.procesar_pago(500))
print(pago1.procesar_pago(2000))
print(pago1.procesar_pago(400))




# Practica: Introducción al polimorfismo con notificaciones

class NotificacionCorreo:
    def enviar(self, mensaje):
        return f"Enviando correo: {mensaje}"

class NotificacionSMS:
    def enviar(self, mensaje):
        return f"Enviando SMS: {mensaje}"

class NotificacionPush:
    def enviar(self, mensaje):
        return f"Enviando notificación push: {mensaje}"

class NotificacionWhatsApp:
    def enviar(self, mensaje):
        return f"Enviando WhatsApp: {mensaje}"

# Instancias
noti1 = NotificacionCorreo()
noti2 = NotificacionSMS()
noti3 = NotificacionPush()
noti4 = NotificacionWhatsApp()

#ejemplo de polimorfismo
print(noti1.enviar("Correo enviado"))
print(noti1.enviar("SMS enviado"))
print(noti1.enviar("Notificación push enviada"))
print(noti1.enviar("WhatsApp enviado"))

