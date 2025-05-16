# Remolintintin

Laboratorios = 2
# Se define el número de filas en cada laboratorio
filas = 5

# Se define cuántas computadoras hay por fila
computadoras_por_fila = 4

# El bucle principal es para cada laboratorio. 
# NOTA: Falta la línea 'laboratorios = 2', está comentada arriba. Debe descomentarse para funcionar.
for lab in range(laboratorios):  
    print(f"\nLaboratorio {lab + 1}")  # Muestra el número del laboratorio actual (comienza desde 1)
    
    computadoras = ()  # Se inicializa una tupla vacía que almacenará las filas del laboratorio

    # Bucle para recorrer cada fila del laboratorio
    for fila_num in range(filas):
        fila = ()  # Se crea una tupla vacía para almacenar el estado de las computadoras de esta fila

        # Bucle para recorrer cada computadora en la fila actual
        for comp_num in range(computadoras_por_fila):
            # Se pide al usuario que ingrese el estado de cada computadora (Ocupada o Libre)
            estado = input(f"Ingrese el estado de la computadora {comp_num + 1} (Ocupada/Libre): ")
            fila = fila + (estado,)  # Se agrega el estado a la tupla 'fila'

        computadoras = computadoras + (fila,)  # Se agrega la fila completa a la tupla de computadoras del laboratorio

    # Inicialización de contadores para los estados
    Ocupada = 0
    Libre = 0

    # Recorre todas las filas y sus computadoras para contar cuántas están Ocupadas o Libres
    for fila in computadoras:
        for estado in fila:
            if estado == "Ocupada":
                Ocupada += 1
            elif estado
