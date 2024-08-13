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

import preparar_pizza
import seleccionar_ingredientes
import calcular_tiempo

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

preparar_pizza.preparar_pizza()
seleccionar_ingredientes.seleccionar_ingredientes()
tiempo_preparacion = calcular_tiempo.calcular_tiempo()
print(f"Su orden ha sido confirmada. La pizza estará lista en aproximadamente {tiempo_preparacion} minutos.")