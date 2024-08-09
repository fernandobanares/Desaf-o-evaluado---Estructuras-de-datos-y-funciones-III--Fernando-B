""" 1. Un menú interactivo que permita al usuario personalizar su Pizza. Para ello,
considera: (6 puntos)
a. Que se permita cambiar el tipo de masa. Actualmente la Pizzería trabaja con
Masa Tradicional, Masa Delgada y Masa con Bordes de Queso.
b. Que se permita cambiar el tipo de salsa. Actualmente la Pizzería trabaja con
Salsa de Tomate, Salsa Alfredo, Salsa Barbecue y Salsa Pesto
c. Que se permita modificar ingredientes (agregar y eliminar). Actualmente, la
pizzería trabaja con los siguientes ingredientes: Tomate, Champiñones,
Aceituna, Cebolla, Pollo, Jamón, Carne, Tocino, Queso
2. Una estimación de tiempo que tomará en que la pizza esté lista, y ofrezca la
posibilidad de confirmar si es que desea ordenar. El tiempo para estar lista serán 20
minutos + 2 minutos por cada ingrediente, excluyendo masa y salsa. (3 puntos)
3. Una opción que permita mostrar los ingredientes que actualmente tiene la pizza. (1
punto) """

""" masa = {"m1":"Tradicional", "m2":"Delgada", "m3":"Borde de queso"}
salsa = {"s1":"Salsa de tomate", "s2":"Salsa Alfredo", "s3":"Salsa barbecue", "s4":"Salsa pesto"}
ingredientes = {"i1":"Tomate","i2":"Champiñones","i3":"Aceituna","i4":"Cebolla","i5":"Pollo","i6":"Jamón","i7":"Carne","i8":"Tocino","i9":"Queso"} """


masa = ["Tradicional", "Delgada", "Borde de queso"]
salsa = ["Salsa de tomate", "Salsa Alfredo", "Salsa barbecue", "Salsa pesto"]
ingredientes = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

msg = "\n--------------------------\n"
msg += "            MENU\n"
msg += "\n--------------------------\n\n"

msg += "Tipos de Masa:\n"
for i in masa:
    msg += " - " + i + "\n"

msg += "\nTipos de Salsa:\n"
for i in salsa:
    msg += " - " + i + "\n"

msg += "\nIngredientes:\n"
for i in ingredientes:
    msg += " - " + i + "\n"
    
msg += "\n--------------------------\n\n"
msg += "Bienvenido a Pizza Jat\n"
print(msg)

def preparar_pizza():
    while True:
        tipo_masa = str(input("Ingrese su tipo de masa: ")).lower()
        if tipo_masa in [m.lower() for m in masa]:
            break
        else:
            print("Por favor, elija entre los tipos de masa del menú.")

    while True:
        tipo_salsa = str(input("Ingrese su tipo de salsa: ")).lower()
        if tipo_salsa in [s.lower() for s in salsa]:
            break
        else:
            print("Por favor, elija entre los tipos de salsa del menú.")

ingredientes_seleccionados = []

def seleccionar_ingredientes():
    while True:
        accion = str(input("Ingrese 'agregar' para añadir un ingrediente, 'quitar' para eliminar uno, 'ver' para mostrar los ingredientes seleccionados o 'terminar' para finalizar: ")).lower()

        if accion == "terminar":
            break

        elif accion == "ver":
            print("Ingredientes seleccionados actualmente:")
            for ing in ingredientes_seleccionados:
                print(f" - {ing.capitalize()}")

        elif accion == "agregar":
            ingrediente = str(input("Ingrese el nombre del ingrediente: ")).lower()
            if ingrediente in [i.lower() for i in ingredientes] and ingrediente not in ingredientes_seleccionados:
                ingredientes_seleccionados.append(ingrediente)
                print(f"{ingrediente.capitalize()} ha sido agregado a tu pizza.")
            elif ingrediente in ingredientes_seleccionados:
                print(f"{ingrediente.capitalize()} ya está en tu pizza.")
            else:
                print("Ese ingrediente no está en la lista disponible.")
        
        elif accion == "quitar":
            ingrediente = str(input("Ingrese el nombre del ingrediente: ")).lower()
            if ingrediente in ingredientes_seleccionados:
                ingredientes_seleccionados.remove(ingrediente)
                print(f"{ingrediente.capitalize()} ha sido quitado de tu pizza.")
            else:
                print(f"{ingrediente.capitalize()} no está en tu pizza.")

def calcular_tiempo_preparacion():
    tiempo_base = 20  # 20 minutos base
    tiempo_por_ingrediente = 2 * len(ingredientes_seleccionados)  # 2 minutos por cada ingrediente
    tiempo_total = tiempo_base + tiempo_por_ingrediente
    return tiempo_total

def confirmar_orden():
    while True:
        confirmar = input("¿Desea confirmar su orden? (sí/no): ").lower()
        if confirmar == "sí":
            tiempo_preparacion = calcular_tiempo_preparacion()
            print(f"Su orden ha sido confirmada. La pizza estará lista en aproximadamente {tiempo_preparacion} minutos.")
            break
        elif confirmar == "no":
            print("Orden cancelada.")
            break
        else:
            print("Respuesta no válida, por favor ingrese 'sí' o 'no'.")

# Ejecución del programa
preparar_pizza()
seleccionar_ingredientes()
tiempo_preparacion = calcular_tiempo_preparacion()
print(f"Su orden ha sido confirmada. La pizza estará lista en aproximadamente {tiempo_preparacion} minutos.")

    
        
    
