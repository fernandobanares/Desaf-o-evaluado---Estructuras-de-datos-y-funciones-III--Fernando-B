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