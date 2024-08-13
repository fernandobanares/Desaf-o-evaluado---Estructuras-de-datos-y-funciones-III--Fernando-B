def calcular_tiempo_preparacion():
    tiempo_base = 20
    tiempo_por_ingrediente = 2 * len(ingredientes_seleccionados)
    tiempo_total = tiempo_base + tiempo_por_ingrediente
    return tiempo_total