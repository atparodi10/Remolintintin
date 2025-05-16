# Nombres de los edificios
edificio1 = "Edificio A"
edificio2 = "Edificio B"
edificio3 = "Edificio C"
edificio4 = "Edificio M"

# Nombres de los turnos
turno1 = "Mañana"
turno2 = "Tarde"
turno3 = "Noche"

# Número de días en la semana
dias_semana = 7

print("Monitoreo del Consumo Energético Semanal")
print("Ingrese los consumos en kWh para cada edificio, turno y día.\n")

# Repetir para cada edificio
for edificio in [edificio1, edificio2, edificio3, edificio4]:
    consumo_total = 0
    dia = 1
    print(f"Edificio: {edificio}")
    
    while dia <= dias_semana:
        print(f"Día {dia}:")
        
        # Solicitar consumos para cada turno
        consumo_total += float(input(f"  Consumo en turno {turno1}: "))
        consumo_total += float(input(f"  Consumo en turno {turno2}: "))
        consumo_total += float(input(f"  Consumo en turno {turno3}: "))
        
        dia += 1
    
    promedio = consumo_total / dias_semana
    print(f"\nTotal semanal en {edificio}: {consumo_total:.2f} kWh")
    print(f"Promedio diario en {edificio}: {promedio:.2f} kWh\n")
