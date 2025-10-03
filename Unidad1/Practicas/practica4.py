import os
os.system('cls')

class Ticket:
    def __init__(self, id, tipo, prioridad, estado="pendiente"):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = estado

    def ticket_imp(self):
        return (
            "----------------------------------\n"
            f"        TICKET #{self.id}\n"
            "----------------------------------\n"
            f"Tipo      : {self.tipo}\n"
            f"Prioridad : {self.prioridad}\n"
            f"Estado    : {self.estado}\n"
            "----------------------------------"
        )

ticket1 = Ticket(1, "software", "alta")
ticket2 = Ticket(2, "prueba", "media")

print(ticket1.ticket_imp())
print()
print(ticket2.ticket_imp())

class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

empleado1 = Empleado("Juan", "Soporte")
empleado1.trabajar_en_ticket(ticket1)

class Desarrollador(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print(f"El desarrollador {self.nombre} ha resuelto el ticket {ticket.id}")
        else:
            print(f"El desarrollador {self.nombre} no puede resolver el ticket {ticket.id} de tipo {ticket.tipo}")

empleado1 = Desarrollador("Ana", "Sofware")
empleado1.trabajar_en_ticket(ticket1) 

class Tester(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print(f"El tester {self.nombre} ha resuelto el ticket {ticket.id}")
        else:
            print(f"El tester {self.nombre} no puede resolver el ticket {ticket.id} de tipo {ticket.tipo}")
empleado1 = Desarrollador("Ane", "Prueba")
empleado1.trabajar_en_ticket(ticket1) 

print()
print("-----Asignación de tickets-----")
class ProjectManager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"El Project Manager {self.nombre} asigna el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)
pm1 = ProjectManager("Carlos", "PM")
pm1.asignar_ticket(ticket1, empleado1)  # Asignar a Desarrollador
pm1.asignar_ticket(ticket2, empleado1)  # Asignar a Desarrollador (no puede resolver)
tester1 = Tester("Luis", "Tester")
pm1.asignar_ticket(ticket2, tester1)  # Asignar a Tester
pm1.asignar_ticket(ticket1, tester1)  # Asignar a Tester (no puede resolver)

#Crear tickets y empleados (Instancias de objetos)
ticket1 = Ticket(1, "software", "alta")
ticket2 = Ticket(2, "prueba", "media")
developer1 = Desarrollador("Gustavo", "Software")
tester1 = Tester("Pablo", "Tester")
pm1 = ProjectManager("Susana", "PM")
pm1.asignar_ticket(ticket1, developer1)


# Parte adicional
# Agregar un menú con while y con if que permita:
#1. Crear un ticket
#2. Ver tickets
#3. Asignar tickets
#4. Salir del programa
def main():
    tickets = []
    empleados = []
    ticket_id = 1
    seguir = True

    while seguir:
        os.system('cls')
        print("\n--- Menú de Tickets ---")
        print("1. Crear ticket")
        print("2. Ver tickets")
        print("3. Registrar empleado")
        print("4. Asignar ticket")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            os.system('cls')
            tipo = input("Tipo de ticket (software/prueba): ")
            prioridad = input("Prioridad (alta/media/baja): ")
            tickets.append(Ticket(ticket_id, tipo, prioridad))
            print(f"Ticket #{ticket_id} creado.")
            ticket_id += 1
            input("Enter para continuar...")

        elif opcion == '2':
            os.system('cls')
            if not tickets:
                print("No hay tickets.")
            else:
                for t in tickets:
                    print(t.ticket_imp())
            input("Enter para continuar...")

        elif opcion == '3':
            os.system('cls')
            print("1. Desarrollador  2. Tester  3. ProjectManager")
            tipo = input("Tipo de empleado (1/2/3): ")
            nombre = input("Nombre: ")
            puesto = input("Puesto: ")
            if tipo == '1':
                empleados.append(Desarrollador(nombre, puesto))
            elif tipo == '2':
                empleados.append(Tester(nombre, puesto))
            elif tipo == '3':
                empleados.append(ProjectManager(nombre, puesto))
            else:
                print("Tipo no válido.")
            input("Enter para continuar...")

        elif opcion == '4':
            os.system('cls')
            if not tickets or not empleados:
                print("Faltan tickets o empleados.")
            else:
                for t in tickets:
                    if t.estado == "pendiente":
                        print(t.ticket_imp())
                        for i, e in enumerate(empleados):
                            print(f"{i+1}. {e.nombre} ({e.puesto})")
                        try:
                            num = int(input("Elige empleado: ")) - 1
                            if 0 <= num < len(empleados):
                                pm = next((e for e in empleados if isinstance(e, ProjectManager)), None)
                                if pm:
                                    pm.asignar_ticket(t, empleados[num])
                                else:
                                    print("No hay Project Manager.")
                            else:
                                print("Número inválido.")
                        except:
                            print("Entrada inválida.")
            input("Enter para continuar...")

        elif opcion == '5':
            seguir = False
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
