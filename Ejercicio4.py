edificios = ["Edificio A", "Edificio B", "Edificio C", "Edificio M"]
turnos = ["Mañana", "Tarde", "Noche"]
dias_semana = 6

print("Monitoreo del Consumo Energético Semanal")
print("Ingrese los consumos en kWh para cada edificio, turno y día.\n")

for edificio in edificios:
    consumo_total = 0
    print(f"\nEdificio: {edificio}")
    for dia in range(1, dias_semana + 1):
        print(f" Día {dia}:")
        for turno in turnos:
            consumo = float(input(f"  Consumo en turno {turno}: "))
            consumo_total += consumo
    promedio = consumo_total / dias_semana
    print(f"\nTotal semanal en {edificio}: {consumo_total:.2f} kWh")
    print(f"Promedio diario en {edificio}: {promedio:.2f} kWh")