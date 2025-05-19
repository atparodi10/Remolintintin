# Registro de asistencia académica

# importamos tabulate de tabulate para poder usar el formato de tabla al momento de imprimir
from tabulate import tabulate

# importamos os para poder acceder a las funciones del sistema operativo
import os

# creamos esta función para limpiar pantalla despues de cada iteracion del ciclo principal
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear") # 'cls' es el comando limpiar pantalla en windows
    # una linea simplificada de if y else para verificar el sistema operativo que se esta utilizando
    
# inicliaziamos los arreglos/listas y variables en las cuales se almacenarán los datos ya conocidos  

aulas = 3 # asiganmos el valor de 3 para indicar las secciones, las cuales seran el rango de iteracion principal
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] # creamos una lista, con el nombre de los 5 dias, este se ocupara para recorrer dia por dia 
estudiantes = 6

# estas son las variables donde se almacenarán el total de asistencias por dias y asi mismo total por semana
total_p = 0
total_nj = 0
total_j = 0

for i in range(aulas): # en este ciclo definimos que la variable i se va a iterar en el rango de inicialización 0 hasta el rango de aulas(3)
    
    print(f"Sección: {i + 1}") # imprimimos el número de seccion segun su rango y le sumamos uno ya que esta inicializada en 0
    
    for dia in dias: # aqui dia representa que en cada iteracion mostrara los valores dentro de la lista días
        print(f"Día: {dia}") # aquí con el formato insertamos el valor de dia segun su iteracion
        
        # Inicializamos las variables que serán uasadas para calcular las asistencias por dia
        presente = 0
        falta_no_justificada = 0
        falta_justificada = 0
        
        for estudiante in range(estudiantes): # este for indica que por cada dia se va iterar 6 veces (1 por estudiante) para aplicar su estado de asistencia 
            while True: # ciclo infinito para iterar una y otra vez hasta que se cumpla la condicion que junto con ella este el break de la misma
                print("=" * 30) # agregamos un separador visual por estudiante
                # Por cada iteración se va mostrando el alumno al cual se le esta asignando la asistencia
                print(f" Estudiante {estudiante + 1} ".center(30, "=")) # .center es una funcion que centra un texto dentro de un ancho fijo.
                # Indicadores para que el usuario ingrese correctamente las opciones validas
                print("Ingrese estado de asistencia:")
                # Se le muestra al usuario las opciones para poder asignar la asistencia tanto como la inicial como la palabra completa
                print(" [P]  Presente") 
                print(" [FNJ] Inasistencia No Justificada")
                print(" [FJ]  Inasistencia Justificada")
                
                # Entrada por teclado donde el usuario ingresa el estado de asistencia y poder realizar las validaciones correspondientes
                asistencia = input(">>").strip().lower() # .strip() para eliminar los espacios en blanco y .lower() para convertir la cadena en minúsculas
                
          
                
                if not asistencia: # El not asistencias es equivalente o lo mismo a decir if asistencia == ""
                    print("⚠️  Campo vacío. Intente nuevamente.\n") # Mensaje de error en dado caso la cadena este vacía
                
                else: # en dado caso que no este vacia realizar lo siguiente
                    if asistencia.replace("-", "").replace(".", "").isdigit(): # .repalce("-", "") para reempalzar carácteres por otros. .isdigit() es para validar si lo ingresado es un entero  
                        print("⚠️  No se aceptan números. Intente nuevamente.\n") # Mensaje de error en dado caso sea un dígito
                    
                    # en los siguientes bloques elif se evalúa si lo ingresado por el usuario es lo mismo o es equivalente a las palabras claves para poder asiganar el estado de asistencia
                    elif asistencia == "presente" or asistencia == "p": 
                        presente += 1 # si el usuario ingresa una de las dos opciones validas se le aumenta 1 al contador 
                        break # define el quiebre del ciclo while true, es decir donde se cumpla esta condición se rompe el ciclo para continuar con la otra parte del código
            
                    elif asistencia == "inasistencia no justificada" or asistencia == "fnj":
                        falta_no_justificada += 1
                        break
                    
                    elif asistencia == "inasistencia justificada" or asistencia == "fj":
                        falta_justificada += 1
                        break
                    
                    else: # muestra mensaje de error en dado caso de no ingresar una opción valida
                        print("⚠️  Opción no válida. Intente nuevamente.\n")
    
        # Luego de que se acumulen las variables contadoras por días se le suman a una general donde se acumulan en total por días y así mismo por semana       
        total_p += presente 
        total_nj += falta_no_justificada       
        total_j += falta_justificada        
        
        limpiar_consola() # Mandamos a llamar la funcion para que cada vez que se vuelva a iterar se limpia la pantalla
        # Mostramos por pantalla el resumen o el total de asistencias por día
        print("-"*5,"Resumen por Día","-"*5)
        print(f"Aula: {i + 1}")
        print(f"Día: {dia}")
        print(f"Presentes: {presente}")
        print(f"Faltas No Justificadas: {falta_no_justificada}")
        print(f"Faltas Justificadas: {falta_justificada}\n")

# creamos un arreglo con subarreglos para poder usar la función tabulate para crear una tabla visual para mostrar al usario
resumen_semanal = [ # los corchetes principales son la lista principal
    # aquí creamos la sublistas con su tipo de dato y valor para mostrar y ordenar en la tabla, se separan cada una con , 
    ["Presentes", total_p],
    ["Faltas Injustificadas", total_nj],
    ["Faltas Justificadas", total_j]
    
]

limpiar_consola() # volvemos a llamar a la función para limpiar pantalla y mostrar tabla final
print("\n" + "-"*5 + "REPORTE SEMANAL" + "-"*5) # concatenamos un salto de linea junto con -*5 para mostrar 5 guiones al momento de la impresión
print(f"Dias: {len(dias)}") # imprimimos la cantidad de días en lo que se calcularon las asistencias. .len(dias) es una funcion donde muestra la longitud de la cadena, equivalente a "Días: 5"
print(f"Estudiantes: {estudiantes}") # imprimimos el valor de la varible estudiantes (6)
# Está es la sintaxis para imprimir la tabla con la librería tabulate 
print(tabulate(resumen_semanal, headers=["Tipo de Asistencia", "Cantidad"], tablefmt="grid")) 
#       función tabulate, lista donde se almacenán los valores, headers= son los encabezados de la tabla, y tablefmt= es l tipo de tabla o estilo que le estamos asigando, en este caso grid=(cuadro con bordes)