
funciones = [
    {"pelicula": "Spider-Man: No Way Home", "hora": "18:00"},
    {"pelicula": "The Batman", "hora": "20:30"},
    {"pelicula": "Encanto", "hora": "16:00"},
]

precio_entrada = 50  

reservas = []  

def mostrar_funciones():
    print("Funciones disponibles:")
    for i, f in enumerate(funciones, start=1):
        print(f"{i}. {f['pelicula']} - {f['hora']}")

def hacer_reserva():
    nombre = input("Ingresa tu nombre: ")
    mostrar_funciones()
    opcion = int(input("Selecciona el número de la función que quieres ver: "))
    funcion = funciones[opcion - 1]
    cantidad = int(input("Cantidad de boletos a comprar: "))
    total = cantidad * precio_entrada

    reserva = {
        "cliente": nombre,
        "pelicula": funcion['pelicula'],
        "hora": funcion['hora'],
        "cantidad": cantidad,
        "total": total
    }

    reservas.append(reserva)

    print("\nResumen de tu reserva:")
    print(f"Cliente: {nombre}")
    print(f"Película: {funcion['pelicula']}")
    print(f"Hora: {funcion['hora']}")
    print(f"Boletos: {cantidad}")
    print(f"Total a pagar: Q{total}")

def mostrar_reservas():
    if not reservas:
        print("No hay reservas aún.")
        return
    print("\nReservas hechas hasta el momento:")
    for r in reservas:
        print(f"{r['cliente']} - {r['pelicula']} - {r['hora']} - {r['cantidad']} boletos - Total: Q{r['total']}")
def cancelar_reserva():
    nombre = input("Ingresa tu nombre para cancelar la reserva: ")
    for i, r in enumerate(reservas):
        if r["cliente"].lower() == nombre.lower():
            print(f"Cancelando reserva de {r['pelicula']} a las {r['hora']}")
            reservas.pop(i)
            print("Reserva cancelada.")
            return
    print("No se encontró reserva con ese nombre.")



def menu():
    while True:
        print("\n--- Sistema CineFácil ---")
        print("1. Hacer una reserva")
        print("2. Mostrar todas las reservas")
        print("3.Cancelar reserva")

        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            hacer_reserva()
        elif opcion == "2":
            mostrar_reservas()
        elif opcion == "3":
         cancelar_reserva()

        elif opcion == "4":
            print("¡Gracias por usar CineFácil!")
            break
    else:
            print("Opción no válida, intenta otra vez.")

if __name__ == "__main__":
    menu()
