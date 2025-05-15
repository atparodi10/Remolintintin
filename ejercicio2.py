#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
#campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora
#se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
#valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras
#ocupadas y libres por laboratorio.

laboratorios = 2
filas = 5
computadoras_por_fila = 4

for lab in range(laboratorios):
    print(f"\nLaboratorio {lab + 1}")
    computadoras = ()

    for fila_num in range(filas):
        fila = ()
        for comp_num in range(computadoras_por_fila):
            estado = input(f"Ingrese el estado de la computadora {comp_num + 1} (Ocupada/Libre): ")
            fila = fila + (estado,)
        computadoras = computadoras + (fila,)

    Ocupada = 0
    Libre = 0
    for fila in computadoras:
        for estado in fila:
            if estado == "Ocupada":
                Ocupada += 1
            elif estado == "Libre":
                Libre += 1

    print(f"\nResumen del Laboratorio {lab + 1}:")
    print(f"Computadoras Ocupadas: {Ocupada}")
    print(f"Computadoras Libres: {Libre}")
