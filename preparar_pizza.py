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