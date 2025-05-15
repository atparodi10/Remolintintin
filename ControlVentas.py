# iniciamos con el total general
total_general = 0
# Recorremos los 3 dias del problema
for dia in range(1, 4):
    print(f"\n--- Día {dia} ---")
    total_dia = 0
    # vamos a recorremos los stands del día
    for stand in range(1, 5):
        print(f"\nStand {stand}:")
        total_stand = 0
        # luego recorremos los productos del stand
        for producto in range(1, 4):
            monto = float(input(f"Ingrese el monto de venta del producto {producto}:"))
            total_stand += monto
        # despues se muestra el resumen de los stand
        print(f"Total ventas del stand {stand}: ${total_stand:.2f}")
        total_dia += total_stand
    # se muestra el resumen del día 
    print(f"\nTotal ventas del día {dia}: ${total_dia:.2f}")
    total_general += total_dia
# por ultimo mostramos el total general de la feria
print(f"\n=== Total general de la feria: ${total_general:.2f} ===")